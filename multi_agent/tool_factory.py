"""Dynamic tool construction for the Martian Data multi-agent system."""
from __future__ import annotations

import json
from typing import Any, Iterable, List, Sequence, Tuple, TYPE_CHECKING

import pandas as pd
from langchain_core.tools import BaseTool, StructuredTool
from langchain_ollama import ChatOllama
from pydantic import BaseModel, Field

from . import data_utils

if TYPE_CHECKING:
    from .agents import ToolRequest


class CountryGuess(BaseModel):
    """Structured response for country inference."""

    country: str = Field(..., description="Guessed country name for the event.")


class DynamicToolFactory:
    """Builds runtime tools requested by the task interpreter."""

    def __init__(self, llm: ChatOllama) -> None:
        self.llm = llm

    def build_tools(
        self, requests: Sequence["ToolRequest"]
    ) -> Tuple[List[BaseTool], List[str]]:
        """Create tool instances for the provided requests.

        Returns:
            tools: Newly constructed tools ready for execution.
            notes: Human-readable notes describing successes or skipped requests.
        """
        tools: List[BaseTool] = []
        notes: List[str] = []

        for request in requests:
            template = request.template
            if template == "llm_country_inference":
                tool = self._build_country_inference_tool(request)
                tools.append(tool)
                notes.append(
                    f"Created tool '{request.tool_name}' using llm_country_inference template."
                )
            elif template == "custom_python":
                notes.append(
                    f"Tool '{request.tool_name}' flagged for manual implementation "
                    "(custom_python template). No automatic tool created."
                )
            else:
                notes.append(
                    f"Unknown template '{template}' for tool '{request.tool_name}'. Skipped."
                )

        return tools, notes

    def _build_country_inference_tool(self, request: "ToolRequest") -> BaseTool:
        """Create a tool that infers country values row-by-row using the LLM."""
        guardrails = request.guardrails
        description = request.description
        tool_name = request.tool_name
        structured_llm = self.llm.with_structured_output(CountryGuess)

        def infer_countries(payload: str = "") -> str:
            """Infer countries for each event row and persist the augmented dataset."""
            filename = "processed_country_enriched.csv"
            try:
                payload_data = json.loads(payload) if payload else {}
                if isinstance(payload_data, dict) and payload_data.get("filename"):
                    filename = payload_data["filename"]
            except json.JSONDecodeError:
                pass

            df = data_utils.refresh_raw_dataset()
            guesses: List[str] = []

            for _, row in df.iterrows():
                event_name = str(row.get("Event Name", "") or "")
                continent = str(row.get("Continent", "") or "")
                year = str(row.get("Year", "") or "")

                prompt = {
                    "user_request": request.description,
                    "guardrails": guardrails,
                    "event": {
                        "name": event_name,
                        "continent": continent,
                        "year": year,
                    },
                }

                response = structured_llm.invoke(
                    [
                        (
                            "system",
                            "You infer the most likely country for the provided historical "
                            "event. Respond with a concise country name. "
                            "If uncertain, return 'Unknown'."
                        ),
                        ("human", json.dumps(prompt)),
                    ]
                )

                country_guess = response.country.strip()
                if not country_guess:
                    country_guess = "Unknown"
                guesses.append(country_guess)

            enriched = data_utils.add_or_replace_column(df, "Country", guesses)
            output_path = data_utils.save_processed_dataframe(enriched, filename=filename)
            return (
                f"Inferred countries for {len(enriched)} rows and wrote results to "
                f"{output_path.as_posix()}."
            )

        return StructuredTool.from_function(
            func=infer_countries,
            name=tool_name,
            description=description or "Infer the country for each dataset entry.",
        )

