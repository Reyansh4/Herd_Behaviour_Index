# Herd Behavior Index (HBI) Documentation

## Table of Contents

1. [HBI Overview](#hbi-overview)
2. [Event Dimensions](#event-dimensions)
3. [HBI Segment Matrix](#hbi-segment-matrix)
4. [Dimension Buckets](#dimension-buckets)
5. [Herd Mode Classification](#herd-mode-classification)
6. [Segment Classification](#segment-classification)
7. [Segment Rules](#segment-rules)
8. [Reference Implementation](#reference-implementation)
9. [Unclassified Events](#unclassified-events)
10. [Methodological Principles](#methodological-principles)

---

## HBI Overview

### Purpose

The **Herd Behavior Index (HBI)** quantifies the systemic impact of collective human behavior events, allowing historical analysis, risk assessment, and forecasting. It combines five key dimensions into a single, interpretable score.

---

## Event Dimensions

The HBI framework uses five core dimensions to evaluate collective behavior events:

| Dimension          | Definition                                                          | Scale | Purpose                                                        |
| ------------------ | ------------------------------------------------------------------- | ----- | -------------------------------------------------------------- |
| **Magnitude (M)**  | Size or scale of participation, financial value, or market affected | 1–10  | Captures absolute significance                                 |
| **Spread (S)**     | Geographic or demographic reach of the event                        | 1–10  | Measures propagation across regions or populations             |
| **Intensity (I)**  | Severity or deviation from normal behavior                          | 1–10  | Highlights extremity or disruption                             |
| **Duration (D)**   | Length of the event                                                 | 1–10  | Captures temporal persistence                                  |
| **Outcome/Impact (R)** | Long-term systemic or structural effect                             | 1–10  | Evaluates ultimate consequences on society, policy, or markets |

> **Note:** Event Type (Social, Financial, Consumer, Technology, Industrial) and Trigger/Cause (Fear, Greed, Opportunity, Repression, Hype, Policy) are tracked for interpretive insights but are optional in the core HBI calculation.

---

## HBI Segment Matrix

### Purpose

Segmentation classifies events into actionable categories, revealing patterns and systemic risk profiles. Similar to RFM segmentation in marketing, the HBI Segment Matrix provides a structured framework for understanding collective behavior regimes.

---

## Dimension Buckets

Each dimension is classified into three buckets based on score ranges:

| Dimension     | Low    | Medium | High  |
| ------------- | ------ | ------ | ----- |
| Magnitude (M) | 1–3    | 4–6    | 7–10  |
| Spread (S)    | 1–3    | 4–6    | 7–10  |
| Intensity (I) | 1–3    | 4–6    | 7–10  |
| Duration (D)  | 1–3    | 4–6    | 7–10  |
| Outcome (R)   | 1–3    | 4–6    | 7–10  |

---

## Herd Mode Classification

Herd Mode captures the **mechanism of coordination**, which is not inferable from strength metrics alone.

### Mode Types

Two modes are defined:

| Mode        | Description                                                          |
| ----------- | -------------------------------------------------------------------- |
| **Co-Present** | Coordination occurs primarily through physical co-location          |
| **Diffusive**  | Coordination spreads through networks, media, or multi-region diffusion |

### Mode Inference Rule

Mode is inferred **solely from Spread (S)**, using the existing spread taxonomy:

| Spread (S) | Interpretation          | Mode        |
| ---------- | ----------------------- | ----------- |
| 1–3        | Local to City-Level     | Co-Present  |
| 4–10       | Regional to National    | Diffusive   |

---

## Segment Classification

### Overview

Segments represent dominant behavioral regimes, not descriptive labels. Only structurally strong regimes are auto-classified.

Five segments are defined:

| Segment ID | Segment Name              | Core Idea                                      |
| ---------- | ------------------------- | ---------------------------------------------- |
| **S1**     | Aligned Expansion         | A herd where scale, spread, and duration reinforce each other under controlled emotional intensity, enabling sustained growth or adoption.  |
| **S2**     | Emotion-Driven            | A herd primarily driven by high emotional intensity without long-term stability, leading to unpredictable and context-dependent outcomes.  |
| **S3**     | Volatile Expansion        |     A herd that achieves large scale quickly but fails to persist, often creating the illusion of success without durable impact.  |
| **S4**     | Persistent Friction       | A herd characterized by sustained high emotional intensity over time, resulting in polarization, resistance, or erosion of trust. |
| **S5**     | Low-Energy Diffusion      | A herd with weak emotional activation that diffuses without force, producing background signals rather than actionable movement. |

### Classification Order

Segments are assigned using **regime-dominance ordering**. Stronger and more constraining regimes are evaluated first.

**Classification Order (Critical):**

1. **Persistent Friction (S4)**
2. **Emotion-Driven (S2)**
3. **Volatile Expansion (S3)**
4. **Aligned Expansion (S1)**
5. **Low-Energy Diffusion (S5)** — residual only

---

## Segment Rules

### S4 – Persistent Friction

**Rule:** `IF Intensity = High AND Duration = High`

- Represents sustained emotional pressure
- Often associated with polarization, resistance, or erosion risk

### S2 – Emotion-Driven

**Rule:** `IF Intensity = High AND Duration ≠ High`

- Emotionally charged but unstable
- Outcomes are highly context-dependent

### S3 – Volatile Expansion

**Rule:** `IF Magnitude ≥ Medium AND Spread ≥ Medium AND Duration = Low`

- Large but short-lived
- Common source of overinvestment errors

### S1 – Aligned Expansion

**Rule:** `IF Magnitude ≥ Medium AND Spread ≥ Medium AND Duration ≥ Medium AND Intensity = Medium`

- Balanced regime where growth or adoption can compound

### S5 – Low-Energy Diffusion

**Rule:** `IF Intensity = Low AND Mode = Diffusive`

- Residual category
- Represents background noise rather than actionable movement
- ⚠️ **Note:** S5 is not valid for Co-Present mode

---

## Reference Implementation

### Python Implementation

```python
def classify_segment(M, S, I, D, mode):
    """
    Classify an event into a segment based on dimension values.
    
    Parameters:
        M: Magnitude (1-10)
        S: Spread (1-10)
        I: Intensity (1-10)
        D: Duration (1-10)
        mode: "Co-Present" or "Diffusive"
    
    Returns:
        Segment name as string
    """
    # Helper functions
    def is_low(val):
        return 1 <= val <= 3
    
    def is_medium(val):
        return 4 <= val <= 6
    
    def is_high(val):
        return 7 <= val <= 10
    
    def is_medium_or_above(val):
        return val >= 4
    
    # Classification order (critical)
    
    # S4 – Persistent Friction
    if is_high(I) and is_high(D):
        return "S4 - Persistent Friction"
    
    # S2 – Emotion-Driven
    if is_high(I) and not is_high(D):
        return "S2 - Emotion-Driven"
    
    # S3 – Volatile Expansion
    if is_medium_or_above(M) and is_medium_or_above(S) and is_low(D):
        return "S3 - Volatile Expansion"
    
    # S1 – Aligned Expansion
    if (
        is_medium_or_above(M)
        and is_medium_or_above(S)
        and is_medium_or_above(D)
        and is_medium(I)
    ):
        return "S1 - Aligned Expansion"
    
    # S5 – Low Energy Diffusion
    if is_low(I) and mode == "Diffusive":
        return "S5 - Low Energy Diffusion"
    
    return "Unclassified"
```

---

## Unclassified Events

Some events remain intentionally **unclassified**. This is a feature, not a limitation.

### When Events are Unclassified

This indicates:
- No dominant regime
- High structural complexity
- Context-heavy interpretation required

### Design Philosophy

The framework prioritizes **signal integrity over forced coverage**. This ensures that segments represent meaningful, actionable categories rather than arbitrary classifications.

---

## Relationship to Outcome (R)

### Key Principles

- **Outcome (R) is not predicted by MSID directly**
- **No global linear relationship exists** between MSID and R
- **Outcome is evaluated within segments**, not across all events

### Framework Capabilities

The framework supports:
- **Regime-wise outcome analysis**
- **Mismatch detection** (structure vs result)
- **Risk–reward diagnostics**

---

## Methodological Principles

### Core Principles

1. **Do not mix structure with outcome**
2. **Do not force full coverage**
3. **Prioritize interpretability over accuracy claims**
4. **Treat segmentation as decision support, not prediction**
5. **Allow ambiguity where reality demands it**

---

## Summary

The HBI segmentation framework:

- ✅ Separates behavior, mechanics, and decisions
- ✅ Handles both physical and diffusive collective events
- ✅ Avoids linear assumptions in complex systems
- ✅ Produces stable, explainable strategic regimes
- ✅ Designed to evolve without breaking its core abstractions

---

## Document Version

This methodology is designed to evolve without breaking its core abstractions. For questions or clarifications, refer to the implementation code or contact the development team.
