"""Compares molecular weight between anti- and pro-apoptotic groups using a violin plot."""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#Step 1: Load our properties data
df = pd.read_csv("data/protein_properties.csv")
#Step 2: Create a violon plot comparing molecular_weight across groups
sns.violinplot(data=df, x="group", y="molecular_weight")
#Step 3: Add labels
plt.title("Molecular Weight: Anti-Apoptotic vs Pro-Apoptotic BCL2 Family proteins")
plt.xlabel("Protein Group")
plt.ylabel("Molecular Weight")
#Step 4: Save the plot
plt.savefig("results/molecular_weight_violin.png")
plt.show()
