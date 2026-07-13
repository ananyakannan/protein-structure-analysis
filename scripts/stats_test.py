"""Runs a Mann-Whitney U test comparing instability index between anti- and pro-apoptotic protein groups."""
import pandas as pd
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
