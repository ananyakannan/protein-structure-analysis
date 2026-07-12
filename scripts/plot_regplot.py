import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#Step 1: Load our properties data
df = pd.read_csv("data/protein_properties.csv")
#Step 2: Create a Regplot- instability_index on x-axis, gravy on y-axis
sns.regplot(data=df, x="instability_index", y="gravy")
#Step 3: add labels
plt.title("Comparison of instability_index vs gravy using regplot")
plt.xlabel("Instability_index")
plt.ylabel("Gravy")
#Step 4: save plot
plt.savefig("results/instability_vs_gravy_regplot.png")
plt.show()
