# Herd Behavior Index (HBI) Data Enrichers Definitions

## Table of Contents

- [Herd Behavior Index (HBI) Data Enrichers Definitions](#herd-behavior-index-hbi-data-enrichers-definitions)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Categorical Fields](#categorical-fields)
    - [1. Event Type](#1-event-type)
    - [2. Trigger/Cause](#2-triggercause)
  - [Numeric Dimensions](#numeric-dimensions)
    - [3. Magnitude (M)](#3-magnitude-m)
    - [4. Spread (S)](#4-spread-s)
    - [5. Intensity (I)](#5-intensity-i)
    - [6. Duration (D)](#6-duration-d)
    - [7. Outcome/Impact (R)](#7-outcomeimpact-r)
  - [Score Labeling Framework](#score-labeling-framework)
    - [Magnitude Score Labels](#magnitude-score-labels)
    - [Spread Score Labels](#spread-score-labels)
    - [Intensity Score Labels](#intensity-score-labels)
    - [Duration Score Labels](#duration-score-labels)
    - [Outcome/Impact Score Labels](#outcomeimpact-score-labels)
  - [Summary](#summary)

---

## Overview

The Herd Behavior Index (HBI) uses seven core data fields to evaluate collective behavior events:

- **2 Categorical Fields:** Event Type, Trigger/Cause (one-word values for clarity and consistency)
- **5 Numeric Dimensions:** Magnitude (M), Spread (S), Intensity (I), Duration (D), Outcome/Impact (R) (quantitative 1–10 scores)

This structure ensures clarity, reproducibility, and investor-friendly presentation.

---

## Categorical Fields

### 1. Event Type

**Definition:** Categorizes the event based on its primary domain or context.

**Purpose:** Helps segment herd behavior across different sectors or domains for analysis.

**Fixed Values & Definitions:**

| Event Type | Definition                                                                                    | Example                            |
| ---------- | --------------------------------------------------------------------------------------------- | ---------------------------------- |
| **Social**     | Events driven by collective human action, societal movements, or mass mobilizations.          | 1925 Rand mine strike              |
| **Financial**  | Events primarily related to markets, investments, or economic speculation.                    | 1929 Wall Street Crash             |
| **Consumer**   | Events driven by changes in consumer behavior, trends, or mass adoption of products.          | 1950s post-war consumer boom       |
| **Technology** | Events triggered by adoption or disruption of new technology affecting large populations.     | 1990s Internet adoption surge      |
| **Industrial** | Events related to production, infrastructure, industrial mobilization, or labor organization. | 1935 Italian invasion mobilization |

**Example:** "1925 Rand mine strike" → **Social**

---

### 2. Trigger/Cause

**Definition:** Identifies the main factor that triggered collective behavior in the event.

**Purpose:** Provides insight into why herd behavior emerged, useful for investors and analysts to understand underlying drivers.

**Fixed Values & Definitions:**

| Trigger     | Definition                                                                          | Example                                                  |
| ----------- | ----------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Fear**        | Herd behavior motivated by perceived threat, danger, or uncertainty.                | Panic withdrawals during financial crises                |
| **Greed**       | Herd behavior driven by desire for profit, gain, or material advantage.             | Tulip mania speculation                                  |
| **Opportunity** | Herd behavior triggered by perceived chance to act, benefit, or improve conditions. | Land reform movements, social entrepreneurship movements |
| **Repression**  | Herd behavior in response to oppression, abuse, or unfair restrictions.             | Moroccan urban protests (1934)                           |
| **Hype**        | Herd behavior fueled by media, rumors, or amplified social attention.               | Viral social campaigns or trends                         |
| **Policy**      | Herd behavior initiated due to changes in law, regulations, or government action.   | Pan-African Congress (1926)                              |

**Example:** "Pan-African Congress (1926)" → **Policy**

---

## Numeric Dimensions

### 3. Magnitude (M)

**Definition:** Measures the size or scale of the event in terms of participation, financial value, or market affected.

**Scale:** 1–10 (1 = very small impact, 10 = extreme/historic-level impact)

**Purpose:** Captures the absolute significance of the event.

**Example:** Thousands of workers on strike → **M = 8**

---

### 4. Spread (S)

**Definition:** Quantifies the geographic or demographic reach of the event.

**Scale:** 1–10 (1 = local/limited, 10 = global/multi-sector impact)

**Purpose:** Measures how widely the herd behavior propagated across regions, countries, or sectors.

**Example:** Pan-African Congress involving multiple continents → **S = 9**

---

### 5. Intensity (I)

**Definition:** Assesses the severity or deviation from normal behavior.

**Scale:** 1–10 (1 = minimal/normal, 10 = extreme/unusual)

**Purpose:** Highlights the extremity or disruptive nature of the event.

**Example:** Violent mine strike with arrests → **I = 7**

---

### 6. Duration (D)

**Definition:** Represents the length of time over which the event unfolded.

**Scale:** 1–10 (1 = hours/days, 10 = years/decades)

**Purpose:** Captures temporal persistence of the herd behavior.

**Example:** Strike lasting several weeks → **D = 5**

---

### 7. Outcome/Impact (R)

**Definition:** Measures the long-term consequences or systemic change resulting from the event.

**Scale:** 1–10 (1 = negligible/no change, 10 = historic/significant change)

**Purpose:** Evaluates the ultimate effect of the herd behavior on society, policy, or markets.

**Example:** Foundation of ANC Youth League influencing later political movements → **R = 9**

---

## Score Labeling Framework

Each numeric dimension (M, S, I, D, R) uses a standardized 1–10 scale with clear labels and meanings to prevent ambiguity.

---

### Magnitude Score Labels

**Magnitude = Size or scale of participation, economic value, or market affected**

| Score | Label         | Meaning                                                       |
| ----- | ------------- | ------------------------------------------------------------- |
| 1     | Minimal       | Very small groups or negligible economic activity             |
| 2     | Very Low      | Small-scale involvement or low economic relevance             |
| 3     | Low           | Noticeable but not regionally impactful                       |
| 4     | Moderate-Low  | Larger groups but still limited influence                     |
| 5     | Moderate      | Significant but not major participation                       |
| 6     | Moderate-High | Large groups, meaningful economic footprint                   |
| 7     | High          | Major involvement or high-value impact                        |
| 8     | Very High     | Substantial involvement with near-national relevance          |
| 9     | Extreme       | Large-scale participation; high economic or social disruption |
| 10    | Historic      | Unprecedented magnitude with long-term relevance              |

---

### Spread Score Labels

**Spread = Geographic or demographic coverage**

| Score | Label          | Meaning                               |
| ----- | -------------- | ------------------------------------- |
| 1     | Local          | One town or specific small group      |
| 2     | Multi-Local    | Several towns or adjacent communities |
| 3     | City-Level     | Single major city                     |
| 4     | Regional       | Multiple cities or subregions         |
| 5     | Multi-Regional | Several regions within one country    |
| 6     | National       | Entire nation affected                |
| 7     | Bi-National    | Two or more countries                 |
| 8     | Multi-National | Several countries in one continent    |
| 9     | Continental    | Multiple continents involved          |
| 10    | Global         | Worldwide reach                       |

---

### Intensity Score Labels

**Intensity = Severity, extremeness, or deviation from normal behavior**

| Score | Label         | Meaning                                               |
| ----- | ------------- | ----------------------------------------------------- |
| 1     | Minimal       | Routine-level behavior                                |
| 2     | Very Low      | Slight deviation, limited disruption                  |
| 3     | Low           | Clear deviation but mild impact                       |
| 4     | Moderate-Low  | Noticeable disruption                                 |
| 5     | Moderate      | Strong but manageable intensity                       |
| 6     | Moderate-High | Significant pressure, occasionally violent or extreme |
| 7     | High          | Severe disruption or high emotional intensity         |
| 8     | Very High     | Violent, extreme, or major systemic strain            |
| 9     | Critical      | Very severe abnormal behavior                         |
| 10    | Maximum       | Extreme and unprecedented intensity                   |

---

### Duration Score Labels

**Duration = How long the herd behavior or event lasted**

| Score | Label          | Meaning        |
| ----- | -------------- | -------------- |
| 1     | Momentary      | Hours          |
| 2     | Very Short     | 1–2 days       |
| 3     | Short          | Several days   |
| 4     | Moderate-Short | 1–2 weeks      |
| 5     | Moderate       | Several weeks  |
| 6     | Long           | 1–3 months     |
| 7     | Extended       | Several months |
| 8     | Very Long      | 6–12 months    |
| 9     | Multi-Year     | 1–5 years      |
| 10    | Prolonged      | 5+ years       |

---

### Outcome/Impact Score Labels

**Outcome/Impact = Long-term systemic or structural effect**

| Score | Label            | Meaning                                                |
| ----- | ---------------- | ------------------------------------------------------ |
| 1     | Negligible       | No lasting impact                                      |
| 2     | Very Low         | Minor and short-lived outcomes                         |
| 3     | Low              | Limited influence, minor policy or behavior change     |
| 4     | Moderate-Low     | Some policy or social attention                        |
| 5     | Moderate         | Clear long-term effects but not transformative         |
| 6     | Strong           | Noticeable systemic or cultural influence              |
| 7     | Significant      | Sustained long-term change in policies or institutions |
| 8     | Major            | Large-scale structural or economic shifts              |
| 9     | Transformational | Major national or international transformation         |
| 10    | Historic         | Permanent structural change acknowledged globally      |

---

## Summary

This documentation provides:

- ✅ Clear definitions for all 7 HBI data fields
- ✅ Standardized 1–10 scoring scales with detailed labels
- ✅ Consistent categorical values for Event Type and Trigger
- ✅ Examples for practical application

The framework ensures clarity, reproducibility, and investor-friendly presentation of collective behavior analysis.
