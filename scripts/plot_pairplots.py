"""Generates a pairplot comparing all numeric protein properties at once, colored by anti-/pro-apoptotic group."""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#Step 1: Load our properties data
df = pd.read_csv("data/protein_properties.csv")
#Step 2: Create a pairplot
sns.pairplot(data=df, vars=["length", "molecular_weight", "instability_index", "aromaticity", "gravy"], hue="group")
#Step 3: Add labels
plt.suptitle("Pairplot for protein properties", y=1.02)
#Step 4: Save plot
plt.savefig("results/pairplot_all_properties.png")
plt.show()
