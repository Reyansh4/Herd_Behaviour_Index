# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [1.0.0] - 2026-03-03

### Added

- **Initial public release** of the Herd Behaviour Index (HBI) framework.
- Core documentation:
  - HBI overview, event dimensions, segment matrix, and Herd Mode ([docs/HBI_index_and_segment_matrix.md](docs/HBI_index_and_segment_matrix.md)).
  - Data enricher and score definitions ([docs/data_enrichers_definitions.md](docs/data_enrichers_definitions.md)).
  - EDA strategy and analysis outline ([docs/EDA_Strategy.md](docs/EDA_Strategy.md)).
- Methodology folder: index and segment logic summary, S5 rule (I low and Mode = Diffusive), Mode inference from Spread ([methodology/README.md](methodology/README.md)).
- Case studies:
  - Fall of the Berlin Wall (1989): narrative ([case_studies/berlin_wall_risk_register.md](case_studies/berlin_wall_risk_register.md)), data ([case_studies/example_berlin_wall.csv](case_studies/example_berlin_wall.csv)), and notebook with segment distribution and dimension charts ([case_studies/berlin_wall_case_study.ipynb](case_studies/berlin_wall_case_study.ipynb)).
- Notebooks: Data Enrichment (HBI scoring, country prediction, event description), Feature Engineering (preprocessing, segment assignment, HBI pipelines). Run from repo root; install via `pip install -r requirements.txt`.
- Dashboards folder and sample data ([sample_data/sample_events.csv](sample_data/sample_events.csv)) with gold-layer schema.
- Governance: CONTRIBUTING.md, CODE_OF_CONDUCT.md (Contributor Covenant 2.1), SECURITY.md, issue templates (bug report, feature request), LICENSE (MIT), VERSION, CHANGELOG.

### Security

- `.env` and secret patterns in `.gitignore`; `data/` excluded from version control. No API keys or proprietary data committed.

---

[1.0.0]: https://github.com/your-org/your-repo/releases/tag/v1.0.0
