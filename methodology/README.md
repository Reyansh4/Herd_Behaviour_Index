# Methodology — Data & Index Logic

This folder holds the **data and index logic** for the Herd Behaviour Index (HBI): how dimensions are defined and how segments are assigned.

## Contents

- **`segment.py`** — Canonical segment and Mode logic: `infer_mode(S)`, `classify_segment(M, S, I, D, mode)`, `assign_segment_row(row)`.
- This README summarizes the segment rules.
- Full definitions, score labels, and segment matrix are in the main docs:
  - [HBI index and segment matrix](../docs/HBI_index_and_segment_matrix.md)
  - [Data enrichers definitions](../docs/data_enrichers_definitions.md)

Use from repo root: `from methodology.segment import classify_segment, infer_mode`. Run tests: `pytest tests/`.

## Dimension buckets

Each numeric dimension (M, S, I, D, R) uses a 1–10 scale. For segmentation, values are bucketed as:

| Bucket   | Range  |
|----------|--------|
| Low      | 1–3    |
| Medium   | 4–6    |
| High     | 7–10   |

## Segment rules (summary)

Segments are evaluated in a fixed order (most specific first). **Mode** is inferred from Spread (S): S 1–3 → Co-Present, S 4–10 → Diffusive. Events that match no rule remain **Unclassified**.

| Segment | Name                  | Condition (M, S, I, D in 1–10; Mode from S) |
|---------|-----------------------|-----------------------------------------------|
| **S4**  | Persistent Friction   | I high (7–10) AND D high (7–10) |
| **S2**  | Emotion-Driven        | I high (7–10) AND D not high |
| **S3**  | Volatile Expansion    | M ≥ 4 AND S ≥ 4 AND D low (1–3) |
| **S1**  | Aligned Expansion     | M ≥ 4 AND S ≥ 4 AND D ≥ 4 AND I medium (4–6) |
| **S5**  | Low-Energy Diffusion  | I low (1–3) **AND Mode = Diffusive** (S5 is not valid for Co-Present mode) |

The **canonical** rules and reference implementation are in [HBI index and segment matrix](../docs/HBI_index_and_segment_matrix.md). Implementation: `methodology/segment.py`. The notebooks under `notebooks/Feature_Engineering/` can call these functions; Mode must be inferred from Spread (S) before applying S5.

## Data requirements

For **segment assignment** only, the input table must have numeric columns:

- `Magnitude(M)` or `M`
- `Spread(S)` or `S`
- `Intensity(I)` or `I`
- `Duration(D)` or `D`

**Mode** is inferred from Spread (S): 1–3 → Co-Present, 4–10 → Diffusive. Segment S5 applies only when Mode = Diffusive; the canonical logic is in [docs/HBI_index_and_segment_matrix.md](../docs/HBI_index_and_segment_matrix.md).

## Unclassified events

Events that match no segment rule are left unclassified. This is by design: the framework prioritizes clear, actionable segments over forcing every event into a bucket. Unclassified events can be analyzed separately or reviewed for rule extensions.
