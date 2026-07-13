"""Plots a KDE curve showing the distribution of instability index across all 11 BCL2-family proteins."""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#Step 1: Load our properties data
df = pd.read_csv("data/protein_properties.csv")
#Step 2: Create a KDE plot for instability
sns.kdeplot(data=df, x="instability_index")
#Step 3: Add labels
plt.title("Distribution of the Instability Index - BCL2 Family Proteins")
plt.xlabel("Instability Index")
plt.ylabel("Density")
#Step 4: Save the plot instead of just showing
plt.savefig("results/instability_distribution.png")
plt.show()
