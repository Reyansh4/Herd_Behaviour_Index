"""
Validate sample_data/sample_events.csv against the gold-layer schema.

Expected columns (from data/gold_layer herd_mentality_events_gold_data_v2.csv):
  Year, Event Name, Continent, Event Description, Country, Decade,
  Event Type, Trigger, Magnitude(M), Spread(S), Intensity(I), Duration(D), Outcome/Impact(R),
  Magnitude_label, Spread_label, Intensity_label, Duration_label, Outcome_label,
  Mode, Segment

Run from repo root: python tests/validate_sample_schema.py
Exit 0 if valid, 1 otherwise.
"""

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SAMPLE_CSV = REPO_ROOT / "sample_data" / "sample_events.csv"

REQUIRED_COLUMNS = [
    "Year",
    "Event Name",
    "Continent",
    "Event Description",
    "Country",
    "Decade",
    "Event Type",
    "Trigger",
    "Magnitude(M)",
    "Spread(S)",
    "Intensity(I)",
    "Duration(D)",
    "Outcome/Impact(R)",
    "Magnitude_label",
    "Spread_label",
    "Intensity_label",
    "Duration_label",
    "Outcome_label",
    "Mode",
    "Segment",
]


def main() -> int:
    if not SAMPLE_CSV.exists():
        print(f"Error: {SAMPLE_CSV} not found. Run from repo root.", file=sys.stderr)
        return 1

    import pandas as pd

    df = pd.read_csv(SAMPLE_CSV)
    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        print(f"Error: sample_events.csv missing columns: {missing}", file=sys.stderr)
        return 1

    # Basic dtype check: numeric dimensions 1-10
    for col in ["Magnitude(M)", "Spread(S)", "Intensity(I)", "Duration(D)", "Outcome/Impact(R)"]:
        if not pd.api.types.is_numeric_dtype(df[col]):
            print(f"Error: {col} should be numeric.", file=sys.stderr)
            return 1
        if df[col].min() < 1 or df[col].max() > 10:
            print(f"Error: {col} should be in range [1, 10]. Got min={df[col].min()}, max={df[col].max()}.", file=sys.stderr)
            return 1

    print("OK: sample_events.csv matches gold-layer schema.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
