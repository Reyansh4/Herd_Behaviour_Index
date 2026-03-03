# Case Studies — Example Applications

This folder is intended for **example applications** of the Herd Behaviour Index (HBI) framework: illustrative use cases, sample analyses, or reference implementations that show how to apply HBI in practice.

## Intended use cases

- **Strategy and risk consulting** — Score and segment collective-behavior events for client reports, scenario analysis, or risk registers.
- **Enterprise risk management** — Maintain a consistent event taxonomy and index for internal risk libraries and dashboards.
- **Policy and research** — Use the open methodology for studies, white papers, or academic work with clear attribution.
- **Market and sector analysis** — Compare events across regions, time periods, or segments to identify trends and patterns.

## How to add a case study

1. Create a new markdown file (e.g. `use_case_risk_register.md`) or a small notebook under a subfolder.
2. Describe the context, input data format, and steps (e.g. run enrichment → run segment assignment → summarize by segment).
3. Use only **synthetic or publicly available data**; do not include proprietary or confidential event data.
4. Submit via a pull request; see [CONTRIBUTING.md](../CONTRIBUTING.md).

## Included case study

- **Fall of the Berlin Wall (1989)** — End-to-end pipeline from **minimal input** to full HBI output.
  - **Minimal input:** [`berlin_wall_minimal.csv`](berlin_wall_minimal.csv) — Year, Event Name, Continent only (the starting point).
  - **Pipeline:** The same order of notebooks used in the repo: Event Description → Country → Data Enrichment (Event Type, Trigger, M,S,I,D,R) → Data Preprocessing (labels) → Segment Matrix (Mode, Segment).
  - [`berlin_wall_risk_register.md`](berlin_wall_risk_register.md) — Narrative, pipeline table (which notebook adds which column), dimension scores, Mode (Diffusive), and Segment (S3 – Volatile Expansion).
  - [`example_berlin_wall.csv`](example_berlin_wall.csv) — Single-row CSV with full HBI schema (result of running the pipeline).
  - [`berlin_wall_case_study.ipynb`](berlin_wall_case_study.ipynb) — Shows minimal input, documents the five pipeline steps, loads the full result, verifies segment logic, and plots segment distribution and dimension charts. Run from repository root after `pip install -r requirements.txt`.
