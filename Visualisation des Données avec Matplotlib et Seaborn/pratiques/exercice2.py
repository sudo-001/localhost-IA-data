import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Charger le dataset "tips"
data = sns.load_dataset("tips")

# Afficher un histogramme de total_bill
plt.figure(figsize=(8, 5))
sns.histplot(data['total_bill'], kde=True, bins=20, color='blue')
plt.title("Histogramme de total_bill")
plt.xlabel("Total Bill")
plt.ylabel("Fréquence")
plt.show()

# Tracer un boxplot de tip par sex
plt.figure(figsize=(8, 5))
sns.boxplot(x='sex', y='tip', data=data, palette='pastel')
plt.title("Boxplot de tip par sex")
plt.xlabel("Sex")
plt.ylabel("Tip")
plt.show()

# Afficher une heatmap de la corrélation entre les variables numériques
plt.figure(figsize=(8, 5))
correlation_matrix = data.corr()