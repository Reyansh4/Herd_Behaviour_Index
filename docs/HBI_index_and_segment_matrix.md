# **Herd Behavior Index (HBI) Documentation**

## **1️⃣ Purpose**

The **Herd Behavior Index (HBI)** quantifies the systemic impact of collective human behavior events, allowing historical analysis, risk assessment, and forecasting. It combines five key dimensions into a single, interpretable score.

---

## **2️⃣ Data and Classification**

### **Event Dimensions**

| Dimension          | Definition                                                          | Scale | Purpose                                                        |
| ------------------ | ------------------------------------------------------------------- | ----- | -------------------------------------------------------------- |
| Magnitude (M)      | Size or scale of participation, financial value, or market affected | 1–10  | Captures absolute significance                                 |
| Spread (S)         | Geographic or demographic reach of the event                        | 1–10  | Measures propagation across regions or populations             |
| Intensity (I)      | Severity or deviation from normal behavior                          | 1–10  | Highlights extremity or disruption                             |
| Duration (D)       | Length of the event                                                 | 1–10  | Captures temporal persistence                                  |
| Outcome/Impact (R) | Long-term systemic or structural effect                             | 1–10  | Evaluates ultimate consequences on society, policy, or markets |

**Note:** Event Type (Social, Financial, Consumer, Technology, Industrial) and Trigger/Cause (Fear, Greed, Opportunity, Repression, Hype, Policy) are tracked for interpretive insights but are optional in the core HBI calculation.

---

## **3️⃣ HBI Calculation Framework**

1. **Normalize Inputs**

[
X_{norm} = \frac{X-1}{9} \quad (\text{to scale 0–1})
]

2. **Derive Outcome/Impact (R)**

[
R = w_M \cdot M_{norm} + w_S \cdot S_{norm} + w_I \cdot I_{norm} + w_D \cdot D_{norm}
]

**Suggested weights:**

| Dimension | Weight |
| --------- | ------ |
| M         | 0.3    |
| S         | 0.25   |
| I         | 0.25   |
| D         | 0.2    |

> Optional: include non-linear adjustment for extremes: ( R = R + k \cdot (M_{norm} \cdot I_{norm}) )

3. **Compute HBI**
   [
   \text{HBI} = R
   ]

* HBI normalized 0–1, optionally scaled back to 1–10:

[
\text{HBI}_{scaled} = 1 + 9 \cdot R
]

4. **Reporting**

* Show M, S, I, D separately along with HBI for transparency.
* Optional Event Type / Trigger multipliers for interpretive adjustment.

---

# **HBI Segment Matrix**

## **1️⃣ Purpose**

Segmentation classifies events into actionable categories, revealing patterns and systemic risk profiles. Similar to RFM segmentation in marketing.

---

## **2️⃣ Dimension Buckets**

| Dimension     | Low | Medium | High |
| ------------- | --- | ------ | ---- |
| Magnitude (M) | 1–3 | 4–6    | 7–10 |
| Spread (S)    | 1–3 | 4–6    | 7–10 |
| Intensity (I) | 1–3 | 4–6    | 7–10 |
| Duration (D)  | 1–3 | 4–6    | 7–10 |
| Outcome (R)   | 1–3 | 4–6    | 7–10 |

---

## **3️⃣ Proposed Segments**

| Segment Name                | M           | S      | I          | D           | R           | Description                                                 |
| --------------------------- | ----------- | ------ | ---------- | ----------- | ----------- | ----------------------------------------------------------- |
| Local Short-term Disruption | Low         | Low    | Low/Medium | Low         | Low         | Small, local events with minimal impact                     |
| Regional Moderate Events    | Medium      | Medium | Medium     | Medium      | Medium      | Regional or sectoral events with moderate systemic effects  |
| Global High-Impact Crises   | High        | High   | High       | Medium/High | High        | Major events affecting multiple countries or continents     |
| Slow-Burn Movements         | Medium/High | Medium | Medium     | High        | Medium/High | Long-duration events with gradual systemic effects          |
| Flash Crises                | High        | High   | High       | Low         | Medium/High | Sudden, intense events with rapid impact but short duration |

> **Notes:**
>
> * Buckets can be adjusted based on historical patterns.
> * Segments are interpretable for clients → actionable risk assessment.
> * Clustering methods (K-Means, hierarchical) can be used later to discover data-driven segments.

---

## **4️⃣ Using the Segment Matrix**

1. **Score each event** (M, S, I, D → R → HBI)
2. **Assign segment** based on thresholds or clustering
3. **Report findings**:

   * Count of events per segment
   * Segment evolution over time
   * Risk patterns and forecasted trends

---

## **5️⃣ Value Proposition**

* Combines numeric index (HBI) + actionable segmentation
* Transparent, interpretable, and defensible IP
* Useful for:

  * Historical analysis
  * Scenario planning
  * Investment, policy, and risk decisions
