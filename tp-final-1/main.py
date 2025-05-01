import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

# Chargement des données
df = pd.read_csv("./dataset/fitness_data.csv")

# Évaluation de la qualité des données
print("=== Aperçu des données ===")
print(df.head())
print("\n=== Informations générales ===")
print(df.info())
print("\n=== Valeurs manquantes ===")
print(df.isnull().sum())
print("\n=== Statistiques descriptives ===")
print(df.describe())

# Traitement des valeurs manquantes
df['height_cm'].fillna(df['height_cm'].median(), inplace=True)
df['weight_kg'].fillna(df['weight_kg'].median(), inplace=True)
df['duration_min'].fillna(df['duration_min'].median(), inplace=True)

# Suppression des valeurs aberrantes (IQR)
def remove_outliers_iqr(data, column):
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    return data[(data[column] >= lower) & (data[column] <= upper)]

df = remove_outliers_iqr(df, 'calories_burned')
df = remove_outliers_iqr(df, 'weight_kg')

# Portrait sociodémographique
print("\n=== Statistiques sociodémographiques par genre ===")
print(df.groupby('gender')[['age', 'height_cm', 'weight_kg']].describe())

# Visualisation sociodémographique
sns.boxplot(x='gender', y='age', data=df)
plt.title("Distribution de l'âge selon le genre")
plt.show()

# Tendances par genre et abonnement
print("\n=== Tendances selon genre et type d'abonnement ===")
print(df.groupby(['gender', 'membership_type']).agg({
    'age': 'mean',
    'duration_min': 'mean',
    'calories_burned': 'mean',
    'satisfaction': 'mean'
}))

# Distribution des durées d’entraînement
sns.histplot(df['duration_min'], kde=True)
plt.title("Distribution des durées d'entraînement")
plt.xlabel("Durée (min)")
plt.show()

# Calories brûlées
sns.histplot(df['calories_burned'], kde=True)
plt.title("Distribution des calories brûlées")
plt.xlabel("Calories")
plt.show()

# Heatmap des corrélations
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Heatmap des corrélations")
plt.show()

# Analyse satisfaction
print("\n=== Moyenne de satisfaction par type d'abonnement ===")
print(df.groupby("membership_type")["satisfaction"].mean())

sns.boxplot(x='membership_type', y='satisfaction', data=df)
plt.title("Satisfaction par type d'abonnement")
plt.show()

# Test d'hypothèse : satisfaction homme vs femme
men_satis = df[df["gender"] == "Male"]["satisfaction"]
women_satis = df[df["gender"] == "Female"]["satisfaction"]
t_stat, p_val = stats.ttest_ind(men_satis, women_satis)
print(f"\nTest T de satisfaction (Homme vs Femme) : t={t_stat:.3f}, p={p_val:.3f}")

# Corrélation entre taille et calories brûlées
corr_val, p_val = stats.pearsonr(df['height_cm'], df['calories_burned'])
print(f"\nCorrélation taille vs calories brûlées : r={corr_val:.3f}, p={p_val:.3f}")
