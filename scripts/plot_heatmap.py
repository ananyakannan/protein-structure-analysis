"""Computes and visualizes a correlation matrix across all numeric protein properties using a heatmap."""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#Step 1: Load our properties data
df = pd.read_csv("data/protein_properties.csv")
#Step 2: Select only the numeric columns we want to correlate
numeric_cols = df[["length", "molecular_weight", "instability_index", "aromaticity", "gravy"]]
#Step 3: Compute correleation matrix
corr_matrix = numeric_cols.corr()
#Step 4: Print it first, just to see the raw numbers before plotting
print(corr_matrix)
#Step 5: Creat a heatmap plot for correlation
sns.heatmap(data=corr_matrix, annot=True, cmap="coolwarm")
#Step 6: Add labels
plt.title("Correlation Matrix of Protein Structural Properties")
#Save figure
plt.savefig("results/correlation_heatmap.png")
plt.show()

