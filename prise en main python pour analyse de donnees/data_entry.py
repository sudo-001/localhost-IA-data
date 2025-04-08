import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./dataset/data.csv')

# Affichage des 5 premières lignes et des statistiques descriptives
print(df.head())

# Affichage des statistiques descriptives
print(df.describe())

# Affichage des colonnes
print(df.columns)

# Affichage des types de données
print(df.dtypes)

# Affichage des valeurs uniques de la colonne 'Nom'
print(df['Nom'].unique())

# Affichage des valeurs manquantes
print(df.isnull().sum())

# Affichage des valeurs dupliquées
print(df.duplicated().sum())

# Affichage des valeurs de la colonne 'Nom' sous forme de graphique
plt.figure(figsize=(10, 5))
plt.title("Graphique de la colonne 'Nom'")
plt.xlabel("Index")
plt.ylabel("Valeurs")
plt.plot(df['Age'])
plt.show()
