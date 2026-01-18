# EDA Strategy: Herd Behavior Index (HBI) Gold Layer Data

**Dataset:** `data/gold_layer/herd_mentality_events_gold_data_v2.csv`  
**Sample Size:** 625 events (1925-2025)  
**Features:** 20 columns (temporal, geographic, HBI dimensions, labels, segments)

---

## 1. Data Overview

### Dataset Schema

| Category | Columns | Type | Description |
|----------|---------|------|-------------|
| Temporal | Year, Decade | int64, object | Event year, decade classification |
| Geographic | Continent, Country | object | Geographic identifiers |
| Event | Event Name, Event Description | object | Text fields |
| Classification | Event Type, Trigger | object | Categorical labels (5 types, 6 triggers) |
| HBI Dimensions | M, S, I, D, R | float64 | Numeric scores (1-10 scale) |
| Labels | Magnitude_label, Spread_label, etc. | object | Text labels for dimensions |
| Derived | Mode, Segment | object | Co-Present/Diffusive, S1-S5 segments |

### Data Quality Checks

- Missing values: 11 missing segments (1.76%)
- Range validation: All HBI dimensions within 1-10
- Duplicates: 0 duplicate rows, 3 duplicate event names
- Data types: Validated

---

## 2. Univariate Analysis

### 2.1 Temporal Distribution

**Implemented:**
- Event frequency by year (line plot)
- Event frequency by decade (bar chart)
- HBI dimensions over time with 5-year rolling average

**Metrics:**
- Mean events per year
- Decade-level aggregations

### 2.2 Geographic Distribution

**Implemented:**
- Continent distribution (pie chart, bar chart)
- Top 20 countries by event count
- Average HBI dimensions by continent

### 2.3 Categorical Fields

**Implemented:**
- Event Type distribution (5 categories)
- Trigger distribution (6 categories)
- Event Type × Trigger cross-tabulation (heatmap)

**Findings:**
- Social events: 606 (97%)
- Policy trigger: 220 (35%)

### 2.4 HBI Dimensions

**Implemented:**
- Descriptive statistics (mean, median, std, min, max, quartiles, skewness, kurtosis)
- Distribution plots (histograms with density curves)
- Box plots for outlier detection
- Z-score outlier identification (|z| > 3)

**Dimensions:** Magnitude(M), Spread(S), Intensity(I), Duration(D), Outcome/Impact(R)

### 2.5 Mode & Segment Distribution

**Implemented:**
- Mode distribution: Co-Present (28, 4.5%) vs Diffusive (597, 95.5%)
- Segment distribution: S1-S5 counts and percentages
- Segment cross-tabulations with Event Type, Trigger, Mode, Continent

---

## 3. Bivariate Analysis

### 3.1 Correlation Analysis

**Implemented:**
- Pearson correlation matrix for M, S, I, D, R
- Correlation heatmap
- Strongest correlations identified (|r| > 0.3)

**Key Correlations:**
- Intensity × Magnitude: r = 0.515
- Outcome × Duration: r = 0.378
- Outcome × Magnitude: r = 0.356

### 3.2 Categorical vs Numeric

**Implemented:**
- Average HBI dimensions by Event Type (grouped bar chart)
- Average HBI dimensions by Trigger (grouped bar chart)
- Box plots: Dimension distributions by Event Type
- Box plots: Dimension distributions by Trigger

### 3.3 Geographic vs Dimensions

**Implemented:**
- Average HBI dimensions by continent (grouped bar chart)
- Top countries analysis

### 3.4 Mode & Segment Relationships

**Implemented:**
- Average dimensions by Mode (Co-Present vs Diffusive)
- Average dimensions by Segment (S1-S5)
- Segment cross-tabulation heatmaps

---

## 4. Multivariate Analysis

### 4.1 Dimension Combinations

**Implemented:**
- Pair plot (scatter matrix) for all 5 dimensions
- Correlation analysis across dimensions

### 4.2 Interaction Effects

**Implemented:**
- Event Type × Trigger cross-tabulation
- Segment × Event Type/Trigger/Mode/Continent cross-tabulations

### 4.3 Temporal × Geographic Patterns

**Implemented:**
- HBI dimensions over time (yearly averages, rolling averages)
- Average dimensions by continent
- Decade-level analysis (dimensions, Event Types, Segments)

---

## 5. Temporal Analysis

### 5.1 Time Series

**Implemented:**
- Events per year (1925-2025)
- Events per decade
- HBI dimensions over time with 5-year rolling average

### 5.2 Decade-Level Analysis

**Implemented:**
- Average HBI dimensions by decade (bar chart)
- Dominant Event Types and Triggers per decade
- Event Type distribution by decade (stacked bar charts)
- Segment distribution by decade (stacked area chart)

---

## 6. Geographic Analysis

**Implemented:**
- Continent distribution (pie chart, bar chart)
- Top 20 countries by event count
- Average HBI dimensions by continent

---

## 7. Segment Analysis

**Implemented:**
- Segment distribution (bar chart, pie chart)
- Average HBI dimensions by segment
- Segment cross-tabulations (Event Type, Trigger, Mode, Continent)
- Segment distribution over time (by decade)

**Segment Distribution:**
- S2 (Emotion-Driven): 264 (42.2%)
- S4 (Persistent Friction): 149 (23.8%)
- S1 (Aligned Expansion): 148 (23.7%)
- S3 (Volatile Expansion): 49 (7.8%)
- S5 (Low Energy Diffusion): 4 (0.6%)

---

## 8. Statistical Summary

### Descriptive Statistics

**Implemented:**
- Overall statistics for HBI dimensions (mean, std, min, max, quartiles, skewness, kurtosis)
- Statistics grouped by Segment, Event Type, Trigger, Continent, Decade

### Outlier Detection

**Implemented:**
- Z-score method (|z| > 3)
- Box plot visualization

---

## 9. Data Quality Assessment

**Implemented:**
- Missing values: 11 missing segments identified
- Range validation: All dimensions within 1-10
- Duplicate detection: 0 duplicate rows
- Data type validation

---

## 10. Visualizations

### Generated Plots (22 total, saved to `/dashboards`)

1. HBI dimensions distribution (histograms with density)
2. HBI dimensions box plots
3. Temporal distribution (events over time)
4. HBI dimensions temporal trends (rolling average)
5. Geographic distribution (continents)
6. Top countries
7. HBI dimensions by continent
8. Event Type & Trigger distribution
9. Event Type × Trigger heatmap
10. HBI dimensions by Event Type
11. HBI dimensions by Trigger
12. Box plots by Event Type
13. Box plots by Trigger
14. Correlation matrix heatmap
15. Segment distribution
16. HBI dimensions by Segment
17. Mode analysis
18. Segment cross-tabulation heatmaps (4 plots)
19. Pair plot (scatter matrix)
20. HBI dimensions by decade
21. Event Type by decade
22. Segment distribution by decade

---

## Implementation Status

### Completed

- ✅ Data loading and validation
- ✅ Descriptive statistics
- ✅ Univariate analysis (temporal, geographic, categorical, dimensions)
- ✅ Bivariate analysis (correlations, categorical-numeric relationships)
- ✅ Multivariate analysis (interactions, temporal-geographic patterns)
- ✅ 22 visualizations generated and saved

---

## Tools & Libraries

- **Data:** pandas, numpy
- **Visualization:** matplotlib, seaborn
- **Statistics:** scipy (for z-scores)

---

**Notebook:** `notebooks/Explorative_Data_Analysis/EDA.ipynb`  
**Output:** All visualizations saved to `dashboards/`  
**Status:** Complete
