# Notebooks — Analysis Pipelines

This folder contains Jupyter notebooks for the HBI pipeline: data enrichment and feature engineering.

## Structure

- **`Data_Enrichment/`**
  - **Data_Enrichment_notebook.ipynb** — Main HBI scoring: assigns Event Type, Trigger, and M, S, I, D, R per event using a configured LLM client (e.g. Ollama). Supports batch processing and resume-friendly runs.
  - **Country_Prediction_notebook.ipynb** — Country prediction for events.
  - **Event_Description_notebook.ipynb** — Event description generation.

- **`Feature_Engineering/`**
  - **Data_Preprocessing.ipynb** — Data loading, validation, and preprocessing for downstream steps.
  - **Segment_Matrix.ipynb** — Applies segment rules (S1–S5) to produce the `Segment` column from dimension scores.
  - **HBI_Notebook.ipynb** — HBI calculation and related feature pipelines.

## Running the notebooks

1. **Install dependencies** from the repo root: `pip install -r requirements.txt` (includes pandas, numpy, matplotlib, seaborn, python-dotenv, and the LLM client used for enrichment).
2. **Run from repository root** so that paths resolve correctly: start Jupyter from the project root (e.g. `jupyter notebook` or `jupyter lab`), and use paths relative to the repo root (e.g. `sample_data/sample_events.csv`, `case_studies/example_berlin_wall.csv`). If you open the notebook from a different directory, set `data_path` and other paths in the notebook to match your layout (e.g. absolute paths or `../../sample_data/sample_events.csv` relative to the notebook file).
3. **Python version:** Use Python 3.10 or newer; the default kernel in the notebooks is Python 3.
4. Use **sample data** for testing: point `data_path` to `sample_data/sample_events.csv` to avoid using proprietary data.
5. Do not hardcode API keys or secrets; use environment variables and a local `.env` file (which is gitignored).

## Data paths

- **Input:** Raw or processed event CSV with at least `Year`, `Event Name`, `Continent`, `Event Description` for enrichment; for segment-only runs, the CSV must include `Magnitude(M)`, `Spread(S)`, `Intensity(I)`, `Duration(D)`.
- **Output:** Processed and gold-layer CSVs are typically written under `data/processed/` and `data/gold_layer/`; ensure those directories exist or adjust paths.

See the root [README.md](../README.md) for a high-level Quick Start and [methodology/](../methodology/) for segment and index logic.
