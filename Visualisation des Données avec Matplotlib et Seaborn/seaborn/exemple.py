import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")
# Afficher les 5 premières lignes du DataFrame
print(df.head())


sns.boxplot(x="day", y="total_bill", data=df)
plt.title("Boxplot des factures totales par jour")
plt.show()