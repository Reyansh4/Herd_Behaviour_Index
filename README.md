# Martian Data Agents

This repository now ships with a LangChain + LangGraph multi-agent workflow that inspects and updates
the herd mentality dataset stored in `data/raw/herd_mentality_events.csv`. It still includes a simple
single-agent CLI (`ollama_agent.py`) if you only need basic chat.

## Setup

1. Create/activate the bundled virtual environment (or any Python 3.10+ environment).
2. Install dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

3. Ensure [Ollama](https://ollama.com/) is running and that the model you plan to use is available:

   ```powershell
   ollama serve            # run in a separate terminal
   ollama pull gemma3:1b   # or another model name if preferred
   ```

4. (Optional) Override LangChain/Ollama defaults:

   ```powershell
   $env:OLLAMA_MODEL = "llama3"
   $env:OLLAMA_BASE_URL = "http://localhost:11434"
   $env:OLLAMA_TEMPERATURE = "0.2"
   ```

## Multi-Agent Workflow

The workflow is orchestrated by LangGraph and includes four agents:

1. **Task Interpreter** – understands your request and proposes a tool plan.
2. **Research Agent** – executes dataset-focused tools (preview, filters, summaries).
3. **Response Parser** – converts research output into structured records.
4. **Result Agent** – summarizes what happened and highlights the outcome.

### Run the multi-agent system

```powershell
python multi_agent_app.py --prompt "Add a country column to each herd mentality event."
```

Use `--verbose` to inspect the generated plan, research output, parsed records, and saved file path:

```powershell
python multi_agent_app.py --prompt "..." --verbose
```

If you omit `--prompt`, the script will ask for input interactively.

Outputs are written to `data/processed/` when the parser agent determines that new data should be saved.

## Simple Chat Agent

For a straightforward conversation with the Ollama model:

```powershell
python ollama_agent.py
```

Type at the `You:` prompt; enter `exit` or press `Ctrl+C` to quit.

