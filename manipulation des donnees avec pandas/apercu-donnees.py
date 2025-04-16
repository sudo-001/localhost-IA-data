import pandas as pd

df = pd.read_csv("./dataset/dataset.csv")

print(df.head())  # Affiche les premières lignes
print(df.info())  # Informations sur le DataFrame
print(df.describe())  # Statistiques descriptives
