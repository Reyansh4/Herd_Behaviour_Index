"""CLI runner for the Martian Data multi-agent workflow."""
from __future__ import annotations

import argparse
from pprint import pprint

from multi_agent.agents import build_agent_bundle
from multi_agent.workflow import build_workflow, WorkflowState


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run the Martian Data multi-agent system on a user request."
    )
    parser.add_argument(
        "--prompt",
        help="User request describing the task for the agents. "
        "If omitted, an interactive prompt will be shown.",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print intermediate artifacts (plan, research output, parser notes).",
    )
    return parser.parse_args()


def run_once(user_prompt: str, *, verbose: bool = False) -> None:
    bundle = build_agent_bundle()
    workflow = build_workflow(bundle)

    final_state: WorkflowState = workflow.invoke({"user_request": user_prompt})
    summary = final_state.get("result_summary")

    if verbose:
        plan = final_state.get("plan_text")
        research_output = final_state.get("research_output_text")
        parser_output = final_state.get("parser_output")

        print("\n=== Task Plan ===")
        print(plan or "(no plan)")

        print("\n=== Research Output ===")
        print(research_output or "(empty)")

        if parser_output:
            print("\n=== Parsed Records ===")
            pprint(parser_output.records)
            print(f"Suggested filename: {parser_output.filename or '(none)'}")
            print(f"Parser notes: {parser_output.notes}")

        processed_path = final_state.get("processed_path")
        if processed_path:
            print(f"\nProcessed file written to: {processed_path}")

        print("\n=== Final Summary ===")

    if summary:
        print(f"\nOverview: {summary.overview}")
        print(f"Data Changes: {summary.data_changes}")
        print(f"Follow-up: {summary.follow_up}")
    else:
        print("Workflow completed but no final summary was produced.")


def main() -> None:
    args = parse_args()

    if args.prompt:
        run_once(args.prompt, verbose=args.verbose)
        return

    bundle = build_agent_bundle()
    workflow = build_workflow(bundle)

    print("Martian Data multi-agent REPL. Type 'exit' or 'quit' to stop.")
    while True:
        try:
            user_prompt = input("\nEnter your analysis request: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not user_prompt:
            continue

        if user_prompt.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        final_state: WorkflowState = workflow.invoke({"user_request": user_prompt})
        summary = final_state.get("result_summary")

        if args.verbose:
            plan = final_state.get("plan_text")
            research_output = final_state.get("research_output_text")
            parser_output = final_state.get("parser_output")

            print("\n=== Task Plan ===")
            print(plan or "(no plan)")

            print("\n=== Research Output ===")
            print(research_output or "(empty)")

            if parser_output:
                print("\n=== Parsed Records ===")
                pprint(parser_output.records)
                print(f"Suggested filename: {parser_output.filename or '(none)'}")
                print(f"Parser notes: {parser_output.notes}")

            processed_path = final_state.get("processed_path")
            if processed_path:
                print(f"\nProcessed file written to: {processed_path}")

            print("\n=== Final Summary ===")

        if summary:
            print(f"\nOverview: {summary.overview}")
            print(f"Data Changes: {summary.data_changes}")
            print(f"Follow-up: {summary.follow_up}")
        else:
            print("Workflow completed but no final summary was produced.")


if __name__ == "__main__":
    main()

