# Dashboards — Visualization Scripts and Outputs

This folder holds **visualization scripts and outputs** for the Herd Behaviour Index (HBI) project: charts, heatmaps, and dashboard assets produced from the analysis pipelines.

## Contents

- **Scripts:** Visualization code may live here or in notebooks under `notebooks/` (e.g. EDA or Feature Engineering). Outputs (plots, exports) can be saved to this directory.
- **Assets:** Binary dashboard files (e.g. `.pbix`) may be placed here if they are generated or shared; ensure no proprietary or confidential data is embedded before committing.

## Usage

- Run the relevant notebooks (see `notebooks/README.md`) to regenerate figures.
- Use **sample data** or synthetic datasets when generating visuals for the repository; do not commit outputs that contain proprietary event data.

See [docs/EDA_Strategy.md](../docs/EDA_Strategy.md) for a list of visualizations and analysis strategy.
