"""Plots a histogram showing the distribution of molecular weight across all 11 BCL2-family proteins."""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#Step 1: Load our properties data
df = pd.read_csv("data/protein_properties.csv")
#Step 2: Create a histogram of molecular weight
sns.histplot(data=df, x="molecular_weight", bins=5)
#Step 3: Add labels 
plt.title("Distribution of Molecular Weight - Bcl2 Family Proteins")
plt.xlabel("Molecular Weight (Daltons)")
plt.ylabel("Count")
#Step 4: Save the plot instead of just showing it
plt.savefig("results/molecular_weight_distribution.png")
plt.show()

