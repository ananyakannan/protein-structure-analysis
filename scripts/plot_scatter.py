import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#Step 1: Load our properties data
df = pd.read_csv("data/protein_properties.csv")
#Step 2: Create a scatter plot - length on x-axis, molecular_weight on y-axis
sns.scatterplot(data=df, x="length", y="molecular_weight")
#Step 3: Add lables
plt.title("Comparison of Length vs Molecular Weight using scatterplot")
plt.xlabel("Length")
plt.ylabel("Molecular Weight")
#Step 4: Save the plot
plt.savefig("results/length_vs_molecular_weight_scatter.png")
plt.show()
