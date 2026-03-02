# Sample Data

This folder contains **synthetic data** for testing the HBI pipeline without using proprietary or confidential event data.

## Files

- **`sample_events.csv`** — Small set of synthetic events (10 rows) with the **same schema** as `data/gold_layer/herd_mentality_events_gold_data_v2.csv`:
  - `Year`, `Event Name`, `Continent`, `Event Description`, `Country`, `Decade`
  - `Event Type`, `Trigger`
  - `Magnitude(M)`, `Spread(S)`, `Intensity(I)`, `Duration(D)`, `Outcome/Impact(R)`
  - `Magnitude_label`, `Spread_label`, `Intensity_label`, `Duration_label`, `Outcome_label`
  - `Mode` (Co-Present / Diffusive), `Segment` (e.g. S1 - Aligned Expansion, S2 - Emotion-Driven)

All events are fictional and for illustration only.

## Usage

- **Segment assignment only:** Use this file as input to `notebooks/Feature_Engineering/Segment_Matrix.ipynb`. Set `data_path` to the path of `sample_events.csv` (e.g. `../../sample_data/sample_events.csv` relative to the notebook).
- **Full pipeline:** If your enrichment step expects only `Year`, `Event Name`, `Continent`, `Event Description`, you can use the same file; the notebook will produce or overwrite Event Type, Trigger, and dimension scores. For segment assignment, ensure the CSV has the numeric dimension columns after enrichment.

Do not commit proprietary or real event datasets to this folder. See [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines on contributing additional synthetic or public datasets.
