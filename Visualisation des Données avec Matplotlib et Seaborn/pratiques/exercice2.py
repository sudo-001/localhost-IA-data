import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

# Histogramme de total_bill
sns.histplot(df['total_bill'], bins=20, kde=True, color='skyblue')
plt.title("Répartition des additions")
plt.show()

# Boxplot de tip par sexe
sns.boxplot(x='sex', y='tip', data=df, palette="Set2")
plt.title("Pourboires par sexe")
plt.show()

# Heatmap de corrélations
import pandas as pd
correlation_matrix = df.corr(numeric_only=True)

sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title("Matrice de corrélation")
plt.show()
