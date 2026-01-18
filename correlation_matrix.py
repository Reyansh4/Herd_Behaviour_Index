import seaborn as sns
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

data_path = Path("data/gold_layer/herd_mentality_events_gold_data_v1.csv").resolve()

dashboards_dir = Path("dashboards")
output_path = dashboards_dir / "correlation_matrix.png"
data = pd.read_csv(data_path)

# Select HBI dimensions
hbi_cols = ['Magnitude(M)', 'Spread(S)', 'Intensity(I)', 'Duration(D)', 'Outcome/Impact(R)']
hbi_data = data[hbi_cols]

# Calculate correlation matrix
corr_matrix = hbi_data.corr()

# Create heatmap
plt.figure(figsize=(10, 8))
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))  # Optional: mask upper triangle
sns.heatmap(corr_matrix, 
            annot=True, 
            fmt='.2f', 
            cmap='coolwarm', 
            center=0,
            square=True,
            linewidths=0.5,
            cbar_kws={"shrink": 0.8},
            mask=None)  # Set mask=None to show full matrix, or mask=mask for upper triangle

plt.title('HBI Dimensions Correlation Matrix', fontsize=16, fontweight='bold', pad=20)
plt.tight_layout()

# Save to dashboards folder
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Correlation matrix saved to: {output_path}")
plt.show()