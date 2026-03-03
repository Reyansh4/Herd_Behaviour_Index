# Case Study: Fall of the Berlin Wall (1989) — Risk Register Tagging

This case study shows how the HBI framework is used to tag a single high-impact historical event for strategy and risk analysis. The **Fall of the Berlin Wall** is used as an illustrative example: we start from **minimal input** (Year, Event Name, Continent) and run the full enrichment pipeline to obtain Event Description, Country, Event Type, Trigger, dimension scores (M, S, I, D, R), labels, Mode, and Segment.

---

## 1. Starting point: minimal input

The initial data had only three columns:

| Year | Event Name           | Continent |
|------|----------------------|-----------|
| 1989 | Fall of Berlin Wall  | Europe    |

See [`berlin_wall_minimal.csv`](berlin_wall_minimal.csv).

---

## 2. Pipeline: from minimal input to full HBI output

The repository notebooks are run **in this order** to go from minimal input to the full gold-layer row (with Event Description, Country, Event Type, Trigger, M/S/I/D/R, labels, Mode, Segment):

| Step | Notebook | What it adds |
|------|----------|----------------|
| 1 | [Event_Description_notebook.ipynb](../notebooks/Data_Enrichment/Event_Description_notebook.ipynb) | **Event Description** — narrative text for the event. |
| 2 | [Country_Prediction_notebook.ipynb](../notebooks/Data_Enrichment/Country_Prediction_notebook.ipynb) | **Country** — primary country associated with the event. |
| 3 | [Data_Enrichment_notebook.ipynb](../notebooks/Data_Enrichment/Data_Enrichment_notebook.ipynb) | **Event Type**, **Trigger**, and **M, S, I, D, R** (HBI dimension scores 1–10). |
| 4 | [Data_Preprocessing.ipynb](../notebooks/Feature_Engineering/Data_Preprocessing.ipynb) | **Label columns** — Magnitude_label, Spread_label, Intensity_label, Duration_label, Outcome_label (text labels for each score). |
| 5 | [Segment_Matrix.ipynb](../notebooks/Feature_Engineering/Segment_Matrix.ipynb) | **Mode** (Co-Present / Diffusive, inferred from Spread) and **Segment** (S1–S5). |

After running this pipeline, the Berlin Wall event has the full schema as in [`example_berlin_wall.csv`](example_berlin_wall.csv).

---

## 3. Event summary (full output)

| Field | Value |
|-------|--------|
| **Year** | 1989 |
| **Event Name** | Fall of Berlin Wall |
| **Continent** | Europe |
| **Country** | Germany |
| **Decade** | 1980's |
| **Event Type** | Social |
| **Trigger** | Opportunity |

---

## 4. Dimension scores (1–10)

| Dimension | Score | Label | Rationale (summary) |
|-----------|-------|--------|----------------------|
| **Magnitude (M)** | 9 | Extreme | Massive participation; border openings and reunification scale. |
| **Spread (S)** | 9 | Continental | Impact across Eastern Europe and beyond; continental reach. |
| **Intensity (I)** | 8 | Very High | High emotional and symbolic intensity; peaceful but decisive breach. |
| **Duration (D)** | 2 | Very Short | Key breach and initial celebrations over hours/days; reunification later. |
| **Outcome/Impact (R)** | 9 | Transformational | End of Cold War dynamics; lasting geopolitical and institutional impact. |

---

## 5. Mode and segment

- **Mode:** **Diffusive** (Spread S = 9 → regional to global; coordination via media and multi-region diffusion).
- **Segment:** **S3 – Volatile Expansion**
  - **Rule:** Magnitude ≥ Medium AND Spread ≥ Medium AND Duration = Low.
  - **Interpretation:** The event achieved very large scale and reach quickly but the *peak collective behavior* was short-lived (hours to days). The framework classifies it as Volatile Expansion: big and visible, but the “event” as a discrete episode was brief, with longer-term outcomes (reunification, policy) following afterward.

This supports risk and strategy use cases: e.g. tagging similar “short burst, high impact” events in a risk register, or comparing them to long-duration, high-intensity regimes (S4) or sustained expansion (S1).

---

## 6. How to reproduce

- **Minimal input:** [`berlin_wall_minimal.csv`](berlin_wall_minimal.csv) (Year, Event Name, Continent only).
- **Full output:** [`example_berlin_wall.csv`](example_berlin_wall.csv) — result after running the pipeline above (or use as reference).
- **Notebook:** [`berlin_wall_case_study.ipynb`](berlin_wall_case_study.ipynb) — shows the minimal starting point, documents the pipeline steps, loads the full result, and displays segment distribution and dimension charts.
- **Run from repo root:** `pip install -r requirements.txt`, then run the enrichment notebooks in order (steps 1–5 above) for your own data, or open the case study notebook to inspect the pipeline and the Berlin Wall result.

---

## 7. Takeaway

The Berlin Wall example illustrates the **end-to-end workflow**: start with minimal event data (Year, Event Name, Continent), run the documented notebooks in sequence to add descriptions, country, HBI scores, labels, and segments, then use the full output for risk registers, scenario sets, or historical event libraries.
