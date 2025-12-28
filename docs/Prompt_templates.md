# **HBI GPT Prompt Template (Markdown)**

```markdown
# Herd Behavior Index (HBI) Scoring Prompt

You are analyzing historical events and assigning scores for a Herd Behavior Index (HBI). For each event, you will do two things:

1. Assign **Event Type** and **Trigger**.
2. Assign numeric scores (1–10) for **Magnitude (M), Spread (S), Intensity (I), Duration (D), Outcome/Impact (R)**.

Use the definitions and scales below.

---

## Event Type (choose one)
- Social
- Financial
- Consumer
- Technology
- Industrial

## Trigger (choose one)
- Fear
- Greed
- Opportunity
- Repression
- Hype
- Policy

---

## HBI Scoring Scale (1–10)

- **Magnitude (M):** Size/scale of participation, financial impact, or market affected (1 = very small, 10 = extreme)  
- **Spread (S):** Geographic or demographic reach (1 = local, 10 = global/multi-sector)  
- **Intensity (I):** Severity or deviation from normal behavior (1 = minimal, 10 = extreme)  
- **Duration (D):** Length of time over which the event unfolded (1 = hours/days, 10 = years/decades)  
- **Outcome/Impact (R):** Long-term effect or systemic change (1 = negligible, 10 = historic/significant)  

---

## Few-Shot Examples

**Example 1:**  
Event: "1925 South African Rand mine strike — Thousands of workers on the Witwatersrand launched a coordinated strike for better wages and conditions, resulting in violent clashes and arrests."  
Event Type: Social, Trigger: Repression, M: 8, S: 6, I: 7, D: 5, R: 7  

**Example 2:**  
Event: "1926 Pan-African Congress — African intellectuals and diaspora leaders organized a transcontinental anti-colonial platform, coordinating activism across multiple continents."  
Event Type: Social, Trigger: Policy, M: 6, S: 9, I: 6, D: 4, R: 8  

---

## Instructions for New Events

- Read the event description carefully.  
- Pick **one Event Type** and **one Trigger** from the lists above.  
- Assign numeric scores (1–10) for M, S, I, D, R using the scales provided.  
- Optional: Reason briefly for each score (helps consistency).  
- **Always output in this exact format (CSV-ready):**


Event Type: <value>, Trigger: <value>, M: <value>, S: <value>, I: <value>, D: <value>, R: <value>

## Event Description

<Event Description Here>
```
This format is:

* **Clear & structured**
* **CSV-ready for 600 events**
* Includes **few-shot examples** for consistency
* Optional reasoning (CoT) can be included without breaking output
