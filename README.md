# Herd Behaviour Index (HBI)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](VERSION)

**An Open Source Behavioral Intelligence Framework for Strategy, Risk, and Market Analysis.**

---

## Overview

The **Herd Behaviour Index (HBI)** is a structured framework for quantifying and classifying collective human behavior events. It supports historical analysis, risk assessment, and strategic planning by scoring events along five dimensions (Magnitude, Spread, Intensity, Duration, Outcome/Impact) and assigning them to interpretable segments.

HBI is designed for use in strategy consulting, enterprise risk management, policy research, and market analysis. The methodology is transparent, reproducible, and documented so that teams can adopt it, extend it, or integrate it into existing workflows.

---

## Core Framework

### Event Logic

Each event is characterized by:

- **Event Type** (one of): Social, Financial, Consumer, Technology, Industrial  
- **Trigger** (one of): Fear, Greed, Opportunity, Repression, Hype, Policy  
- **Five numeric dimensions (1–10 scale):**
  - **Magnitude (M)** — Size or scale of participation, economic value, or market affected  
  - **Spread (S)** — Geographic or demographic reach  
  - **Intensity (I)** — Severity or deviation from normal behavior  
  - **Duration (D)** — Time length of the event  
  - **Outcome/Impact (R)** — Long-term systemic or structural effect  

Definitions and score labels are in [`docs/data_enrichers_definitions.md`](docs/data_enrichers_definitions.md) and [`docs/HBI_index_and_segment_matrix.md`](docs/HBI_index_and_segment_matrix.md).

### Segment Model

Events are classified into behavioral segments (S1–S5) using dimension buckets (Low: 1–3, Medium: 4–6, High: 7–10):

| Segment | Name | Rule (summary) |
|--------|------|-----------------|
| **S1** | Aligned Expansion | M,S ≥ Medium, D ≥ Medium, I = Medium |
| **S2** | Emotion-Driven | I = High, D &lt; High |
| **S3** | Volatile Expansion | M,S ≥ Medium, D = Low |
| **S4** | Persistent Friction | I = High, D = High |
| **S5** | Low-Energy Diffusion | I = Low |

Unclassified events are allowed; the framework prioritizes signal integrity over forced coverage. Full rules and implementation details are in [`methodology/`](methodology/).

### HBI Calculation

Dimension scores are normalized to 0–1, combined with fixed weights (e.g. M 0.3, S 0.25, I 0.25, D 0.2), and optionally scaled to a 1–10 index. The exact formula and reporting conventions are documented in [`docs/HBI_index_and_segment_matrix.md`](docs/HBI_index_and_segment_matrix.md) and [`methodology/`](methodology/).

---

## Repository Structure

```
├── docs/                    # Framework explanations and reference
│   ├── HBI_index_and_segment_matrix.md
│   ├── data_enrichers_definitions.md
│   └── EDA_Strategy.md
├── methodology/             # Data and index logic (calculation, segment rules)
│   └── README.md
├── case_studies/            # Example applications and use cases
│   └── README.md
├── notebooks/               # Analysis and enrichment pipelines
│   ├── Data_Enrichment/     # HBI scoring, country prediction, event description
│   └── Feature_Engineering/ # Preprocessing, HBI computation, segment assignment
├── dashboards/              # Visualization scripts and outputs
│   └── README.md
├── sample_data/             # Synthetic data for testing the pipeline
│   └── sample_events.csv
├── data/                    # Local data (raw, processed, gold); not included in repo
│   ├── raw/
│   ├── processed/
│   └── gold_layer/
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── CHANGELOG.md
├── VERSION
└── LICENSE                  # MIT
```

**Documentation (PDF):** To build a single methodology PDF for clients, use [pandoc](https://pandoc.org/):  
`pandoc docs/HBI_index_and_segment_matrix.md docs/data_enrichers_definitions.md -o HBI_methodology.pdf`

---

## Quick Start

### Prerequisites

- Python 3.10+
- pip (or your preferred package manager)

### Setup

```bash
git clone <repository-url>
cd <repository-name>
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

For running the enrichment pipeline with an LLM backend, install the client you use (e.g. `ollama`) and set required environment variables (e.g. API base URL, API key) in a local `.env` file. Do not commit `.env` or any secrets.

### Run with sample data

1. **Use synthetic events** (no proprietary data):

   Place [`sample_data/sample_events.csv`](sample_data/sample_events.csv) in your working directory or point your notebook/script to that path.

2. **Segment assignment only** (no API calls):

   - Open `notebooks/Feature_Engineering/Segment_Matrix.ipynb`
   - Set `data_path` to `sample_data/sample_events.csv` (or your own CSV with columns: `Magnitude(M)`, `Spread(S)`, `Intensity(I)`, `Duration(D)`)
   - Run the cells to compute the `Segment` column

3. **Full pipeline** (enrichment + segments):

   - Ensure your CSV has at least: `Year`, `Event Name`, `Continent`, `Event Description`
   - Run the Data Enrichment notebook to obtain Event Type, Trigger, and M, S, I, D, R (requires configured LLM client)
   - Run Feature Engineering notebooks to compute HBI and Segment

Paths in notebooks are relative to the notebook location; adjust if your repo root differs.

---

## Business & Professional Applications

- **Strategy and risk consulting** — Score and segment collective-behavior events for client reports, scenario analysis, and risk registers.  
- **Enterprise risk management** — Maintain a consistent taxonomy and index for internal event libraries and risk dashboards.  
- **Policy and research** — Use a documented, open methodology for studies and publications.  
- **Market and sector analysis** — Compare events across regions, time periods, or segments for trend and pattern analysis.

The framework is intended as a decision-support tool. It does not replace expert judgment or regulatory requirements.

---

## Limitations

- **Subjectivity:** Dimension and segment assignment can involve judgment; consistency is improved by clear definitions and optional use of LLM-based scoring with human review.  
- **Coverage:** Not all events will match a segment; unclassified events are expected and can be analyzed separately.  
- **Causality:** HBI describes structure and classification of events; it does not infer causation or forecast outcomes.  
- **Data and tooling:** Enrichment pipelines depend on external services (e.g. LLM APIs); sample data and segment logic can be used offline.

---

## License

This project is licensed under the **MIT License**. Commercial use is permitted. See [LICENSE](LICENSE) for the full text.

---

## Attribution

If you use HBI in research, products, or consulting, we ask that you acknowledge the framework and this repository. You may use wording such as:

> “This work uses the Herd Behaviour Index (HBI) framework (MIT License), an open source behavioral intelligence framework for strategy, risk, and market analysis.”

---

## Roadmap

- **v1.0 (2026)** — Initial public release: framework docs, segment rules, enrichment and feature-engineering notebooks, sample data.  
- **v1.x** — Community feedback: improved prompts, additional segment or dimension options, more case studies.  
- **v2.x** — Possible extensions: API layer, optional weighting schemes, integration examples with common analytics platforms.

See [CHANGELOG.md](CHANGELOG.md) for version history and [CONTRIBUTING.md](CONTRIBUTING.md) for how to propose changes.
