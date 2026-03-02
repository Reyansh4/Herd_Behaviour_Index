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

1. Install dependencies from the repo root: `pip install -r requirements.txt` (includes pandas, numpy, matplotlib, seaborn, python-dotenv, and the LLM client used for enrichment).
2. Paths in notebooks are relative to the notebook file; adjust `data_path` if your repo layout differs.
3. Use **sample data** for testing: point `data_path` to `sample_data/sample_events.csv` to avoid using proprietary data.
4. Do not hardcode API keys or secrets; use environment variables and a local `.env` file (which is gitignored).

## Data paths

- **Input:** Raw or processed event CSV with at least `Year`, `Event Name`, `Continent`, `Event Description` for enrichment; for segment-only runs, the CSV must include `Magnitude(M)`, `Spread(S)`, `Intensity(I)`, `Duration(D)`.
- **Output:** Processed and gold-layer CSVs are typically written under `data/processed/` and `data/gold_layer/`; ensure those directories exist or adjust paths.

See the root [README.md](../README.md) for a high-level Quick Start and [methodology/](../methodology/) for segment and index logic.
