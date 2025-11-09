"""LangGraph workflow orchestrating the Martian Data multi-agent system."""
from __future__ import annotations

from typing import Any, Dict, List, Optional

import json
import pandas as pd
from langchain_core.tools import BaseTool
from langgraph.graph import END, StateGraph
from langgraph.graph.state import CompiledStateGraph
from typing_extensions import TypedDict

from .agents import (
    AgentBundle,
    ParserOutput,
    ResultSummary,
    TaskPlan,
    ToolAction,
    base_tool_map,
    build_agent_bundle,
)
from .tool_factory import DynamicToolFactory
from . import data_utils


class WorkflowState(TypedDict, total=False):
    """Shared state passed between graph nodes."""

    user_request: str
    plan: TaskPlan
    plan_text: str
    available_tools: Dict[str, BaseTool]
    tool_build_notes: List[str]
    tool_results: List[Dict[str, Any]]
    research_messages: List[Any]
    research_output_text: str
    parser_output: ParserOutput
    processed_path: Optional[str]
    result_summary: ResultSummary


def _format_plan(plan: TaskPlan) -> str:
    """Render a task plan into human-readable text."""
    action_lines = "\n".join(
        f"- {action.tool_name}({action.arguments}) :: {action.rationale}"
        for action in plan.actions
    )
    request_lines = "\n".join(
        f"- {request.tool_name} (template={request.template}) :: {request.description}"
        for request in plan.tool_requests
    )
    key_columns = ", ".join(plan.key_columns) if plan.key_columns else "none specified"
    return (
        f"Intent: {plan.intent}\n"
        f"Requires writing: {plan.requires_writing}\n"
        f"Relevant columns: {key_columns}\n"
        f"Expected output: {plan.expected_output_description}\n"
        f"Requested tools:\n{request_lines or '- (none)'}\n"
        f"Planned actions:\n{action_lines or '- (no tool executions required)'}"
    )


def _format_result_context(state: WorkflowState) -> str:
    """Create the context string for the result agent."""
    plan_text = state.get("plan_text", "")
    research_output = state.get("research_output_text", "")
    tool_results = state.get("tool_results", [])
    tool_notes = state.get("tool_build_notes", [])
    parser_output = state.get("parser_output")
    processed_path = state.get("processed_path")

    parser_notes = ""
    if parser_output:
        parser_notes = (
            f"Parser notes: {parser_output.notes}\n"
            f"Records parsed: {len(parser_output.records)}\n"
            f"Suggested filename: {parser_output.filename or 'not provided'}"
        )

    file_line = f"Processed file written to: {processed_path}" if processed_path else "No file written."

    return (
        f"User request:\n{state.get('user_request')}\n\n"
        f"Plan:\n{plan_text}\n\n"
        f"Research output:\n{research_output}\n\n"
        f"Tool creation notes:\n{json.dumps(tool_notes, indent=2)}\n\n"
        f"Tool executions:\n{json.dumps(tool_results, indent=2)}\n\n"
        f"{parser_notes}\n"
        f"{file_line}"
    )


def build_workflow(bundle: Optional[AgentBundle] = None) -> CompiledStateGraph:
    """Compile and return the LangGraph workflow for the multi-agent system."""
    agents = bundle or build_agent_bundle()
    graph = StateGraph(WorkflowState)

    def interpret_task(state: WorkflowState) -> Dict[str, Any]:
        plan: TaskPlan = agents.task_interpreter.invoke(
            {"user_request": state["user_request"]}
        )
        updates: Dict[str, Any] = {}

        tool_requests = list(plan.tool_requests)
        if not tool_requests:
            default_request = ToolRequest(
                tool_name="infer_country_predictions",
                template="llm_country_inference",
                description=(
                    "Infer the most likely country for each event in the dataset and persist "
                    "the augmented rows."
                ),
                input_fields=["Event Name", "Continent", "Year"],
                guardrails=(
                    "Return recognized country names or 'Unknown'. Do not fabricate additional "
                    "columns. Ensure output row count matches input row count."
                ),
            )
            tool_requests = [default_request]
            updates["tool_requests"] = tool_requests

        actions = list(plan.actions)
        if not actions:
            default_action = ToolAction(
                tool_name=tool_requests[0].tool_name,
                arguments={"filename": "processed_country_enriched.csv"},
                rationale="Generate country predictions for each event and store the results.",
            )
            actions = [default_action]
            updates["actions"] = actions

        if not plan.requires_writing:
            updates["requires_writing"] = True

        if updates:
            plan = plan.copy(update=updates)

        return {"plan": plan, "plan_text": _format_plan(plan)}

    def prepare_tools(state: WorkflowState) -> Dict[str, Any]:
        plan = state["plan"]
        factory = DynamicToolFactory(agents.llm)
        tool_map = base_tool_map()
        notes: List[str] = []

        if plan.tool_requests:
            new_tools, creation_notes = factory.build_tools(plan.tool_requests)
            for tool in new_tools:
                tool_map[tool.name] = tool
            notes.extend(creation_notes)
        else:
            notes.append("No additional tools requested; using default toolset.")

        return {"available_tools": tool_map, "tool_build_notes": notes}

    def run_research(state: WorkflowState) -> Dict[str, Any]:
        plan = state["plan"]
        plan_text = state["plan_text"]
        user_request = state["user_request"]
        available_tools = state.get("available_tools", {})
        action_outputs: List[Dict[str, Any]] = []
        success = True

        if not plan.actions:
            message = (
                "No actions were provided in the task plan. Unable to execute the research phase. "
                "Please revise the plan to include at least one tool invocation."
            )
            return {
                "tool_results": [{"tool_name": "N/A", "arguments": {}, "result": message}],
                "research_messages": [],
                "research_output_text": message,
                "research_success": False,
            }

        for action in plan.actions:
            tool_entry: Optional[BaseTool] = available_tools.get(action.tool_name)
            if not tool_entry:
                action_outputs.append(
                    {
                        "tool_name": action.tool_name,
                        "arguments": action.arguments,
                        "result": f"Tool '{action.tool_name}' is not available.",
                    }
                )
                success = False
                continue

            input_payload: Any
            if not action.arguments:
                input_payload = ""
            else:
                input_payload = action.arguments
                if isinstance(input_payload, dict):
                    input_payload = json.dumps(input_payload)

            try:
                tool_result = tool_entry.invoke(input_payload)
            except Exception as exc:  # noqa: BLE001
                try:
                    tool_result = tool_entry.invoke(json.dumps(action.arguments))
                except Exception as inner_exc:  # noqa: BLE001
                    tool_result = f"Error executing tool: {exc} / {inner_exc}"
                    success = False

            action_outputs.append(
                {
                    "tool_name": action.tool_name,
                    "arguments": action.arguments,
                    "result": tool_result,
                }
            )

        tool_results_text = json.dumps(action_outputs, indent=2)

        if not success:
            message = (
                "At least one action failed or could not be executed. "
                "Review tool_results for details."
            )
            return {
                "tool_results": action_outputs,
                "research_messages": [],
                "research_output_text": message,
                "research_success": False,
            }

        research_response = agents.research_agent.invoke(
            {
                "user_request": user_request,
                "plan_text": plan_text,
                "tool_results": tool_results_text,
            }
        )
        if hasattr(research_response, "content"):
            research_output_text = getattr(research_response, "content", "")
        else:
            research_output_text = str(research_response)

        return {
            "tool_results": action_outputs,
            "research_messages": [],
            "research_output_text": research_output_text,
            "research_success": True,
        }

    def parse_response(state: WorkflowState) -> Dict[str, Any]:
        if not state.get("research_success"):
            return {}
        research_output = state.get("research_output_text", "")
        parser_output: ParserOutput = agents.response_parser.invoke(
            {"research_output": research_output}
        )
        return {"parser_output": parser_output}

    def persist_results(state: WorkflowState) -> Dict[str, Any]:
        if not state.get("parser_output"):
            return {"processed_path": None}
        parser_output = state.get("parser_output")
        if not parser_output or not parser_output.records:
            return {"processed_path": None}

        dataframe = pd.DataFrame(parser_output.records)
        filename = parser_output.filename or "herd_mentality_processed.csv"
        output_path = data_utils.save_processed_dataframe(dataframe, filename=filename)
        return {"processed_path": output_path.as_posix()}

    def summarize(state: WorkflowState) -> Dict[str, Any]:
        context = _format_result_context(state)
        summary: ResultSummary = agents.result_agent.invoke({"final_context": context})
        return {"result_summary": summary}

    graph.add_node("interpret_task", interpret_task)
    graph.add_node("prepare_tools", prepare_tools)
    graph.add_node("research", run_research)
    graph.add_node("parse", parse_response)
    graph.add_node("persist", persist_results)
    graph.add_node("summarize", summarize)

    graph.set_entry_point("interpret_task")
    graph.add_edge("interpret_task", "prepare_tools")
    graph.add_edge("prepare_tools", "research")
    graph.add_edge("research", "parse")
    graph.add_edge("parse", "persist")
    graph.add_edge("persist", "summarize")
    graph.add_edge("summarize", END)

    return graph.compile()

