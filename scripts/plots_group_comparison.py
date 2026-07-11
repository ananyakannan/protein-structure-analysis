import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#Step 1: Load our properties data
df = pd.read_csv("data/protein_properties.csv")
#Step 2: Creat a boxplot comparing instability_index across groups
sns.boxplot(data=df, x="group", y="instability_index")
#Step 3: Add labels
plt.title("Instability Index: Anti-Apoptotic vs Pro-Apoptotic BCL2 Family Proteins")
plt.xlabel("Protein Group")
plt.ylabel("Instability Index")
#Step 4: Save the plot
plt.savefig("results/instability_boxplot.png")
plt.show()
