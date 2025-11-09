"""Command-line chat agent using LangChain and a local Ollama model.

Run this module to start an interactive REPL backed by your chosen Ollama model.
Environment variables let you override the model settings:

- ``OLLAMA_MODEL`` (default: ``gemma3:1b``)
- ``OLLAMA_BASE_URL`` (default: ``http://localhost:11434``)
- ``OLLAMA_TEMPERATURE`` (default: ``0.0``)
"""
from __future__ import annotations

import os
from typing import Final, List

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_ollama import ChatOllama

DEFAULT_MODEL: Final[str] = "gemma3:1b"
DEFAULT_BASE_URL: Final[str] = "http://localhost:11434"
DEFAULT_TEMPERATURE: Final[float] = 0.0


def get_env_float(name: str, default: float) -> float:
    """Return a float environment variable, falling back to the provided default."""
    raw_value = os.getenv(name)
    if raw_value is None or raw_value.strip() == "":
        return default
    try:
        return float(raw_value)
    except ValueError:
        raise ValueError(f"Environment variable {name} must be a float, got {raw_value!r}.") from None


def build_model() -> ChatOllama:
    """Construct the ChatOllama instance configured from environment variables."""
    model_name = os.getenv("OLLAMA_MODEL", DEFAULT_MODEL)
    base_url = os.getenv("OLLAMA_BASE_URL", DEFAULT_BASE_URL)
    temperature = get_env_float("OLLAMA_TEMPERATURE", DEFAULT_TEMPERATURE)

    return ChatOllama(
        model=model_name,
        base_url=base_url,
        temperature=temperature,
    )


def run_chat() -> None:
    """Start an interactive CLI session with the Ollama-backed agent."""
    chat_model = build_model()
    messages: List = [
        SystemMessage(
            content=(
                "You are a concise, helpful assistant running on a local Ollama model. "
                "Answer clearly and keep responses focused unless the user requests more detail."
            )
        )
    ]

    print("LangChain ↔ Ollama chat (type 'exit' to quit)")
    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not user_input:
            continue

        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        messages.append(HumanMessage(content=user_input))
        response: AIMessage = chat_model.invoke(messages)
        messages.append(response)
        print(f"Agent: {response.content}")


if __name__ == "__main__":
    run_chat()

