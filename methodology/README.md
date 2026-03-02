# Methodology — Data & Index Logic

This folder holds the **data and index logic** for the Herd Behaviour Index (HBI): how dimensions are defined, how the index is calculated, and how segments are assigned.

## Contents

- This README summarizes the calculation and segment rules.
- Full definitions, score labels, and segment matrix are in the main docs:
  - [HBI index and segment matrix](../docs/HBI_index_and_segment_matrix.md)
  - [Data enrichers definitions](../docs/data_enrichers_definitions.md)

## Dimension buckets

Each numeric dimension (M, S, I, D, R) uses a 1–10 scale. For segmentation, values are bucketed as:

| Bucket   | Range  |
|----------|--------|
| Low      | 1–3    |
| Medium   | 4–6    |
| High     | 7–10   |

## Segment rules (summary)

Segments are evaluated in a fixed order (most specific first). Events that match no rule remain **Unclassified**.

| Segment | Name                  | Condition (M, S, I, D in 1–10) |
|---------|-----------------------|----------------------------------|
| **S4**  | Persistent Friction   | I high (7–10) AND D high (7–10) |
| **S2**  | Emotion-Driven        | I high (7–10) AND D not high    |
| **S3**  | Volatile Expansion    | M ≥ 4 AND S ≥ 4 AND D low (1–3) |
| **S1**  | Aligned Expansion     | M ≥ 4 AND S ≥ 4 AND D ≥ 4 AND I medium (4–6) |
| **S5**  | Low-Energy Diffusion | I low (1–3); may be restricted by mode (see docs) |

The reference implementation (Python) is in the [HBI segment matrix doc](../docs/HBI_index_and_segment_matrix.md). The notebooks under `notebooks/Feature_Engineering/` apply these rules to produce the `Segment` column.

## Data requirements

For **segment assignment** only, the input table must have numeric columns:

- `Magnitude(M)` or `M`
- `Spread(S)` or `S`
- `Intensity(I)` or `I`
- `Duration(D)` or `D`

For **full pipeline** (enrichment then segments), the enrichment step expects at least: `Year`, `Event Name`, `Continent`, `Event Description`. Enrichment produces Event Type, Trigger, and M, S, I, D, R; then segment logic is applied.

## Unclassified events

Events that match no segment rule are left unclassified. This is by design: the framework prioritizes clear, actionable segments over forcing every event into a bucket. Unclassified events can be analyzed separately or reviewed for rule extensions.
