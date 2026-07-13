"""Compares instability index between anti- and pro-apoptotic groups using a boxplot, annotated with a Mann-Whitney U test p-value."""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import mannwhitneyu
#Step 1: Load our properties data
df = pd.read_csv("data/protein_properties.csv")
#Step 2: Split the data into two groups based on the 'group' column
anti = df[df["group"] == "anti-apoptotic"]["instability_index"]
pro = df[df["group"] == "pro-apoptotic"]["instability_index"]
#Step 3: Run the Mann-Whitney U test
stat, p_value = mannwhitneyu(anti, pro)
#Step 4: Print the result
print(f"Mann-Whitney U statistic: {stat}")
print(f"P-value: {p_value}")
#Step 5: Creat a boxplot comparing instability_index across groups
sns.boxplot(data=df, x="group", y="instability_index")
#Step 6: Add labels
plt.title("Instability Index: Anti-Apoptotic vs Pro-Apoptotic BCL2 Family Proteins")
plt.xlabel("Protein Group")
plt.ylabel("Instability Index")
plt.ylim(0, 100)
plt.text(0.5, 90, f"Mann-Whitney p = {p_value:.3f}", ha="center")
#Step 7: Save the plot
plt.savefig("results/instability_boxplot.png")
plt.show()
