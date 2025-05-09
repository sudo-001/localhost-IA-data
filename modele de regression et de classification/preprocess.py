import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Chargement des données
df = pd.read_csv("./dataset/dataset.csv")

# Encodage des variables catégorielles
df['Genre'] = df['genre'].replace({
    'Homme': 'Homme',
    'Femme': 'Femme',
    'H': 'Homme',
    'F': 'Femme',
    'feminin': 'Femme',
    'féminin': 'Femme',
    'homme': 'Homme',
    'Femme ': 'Femme'
})  # Harmonisation

df['Genre'] = LabelEncoder().fit_transform(df['Genre'])  # 0, 1, 2 selon les genres distincts
df['Profession'] = LabelEncoder().fit_transform(df['profession'])
df['Achat'] = LabelEncoder().fit_transform(df['achat'])  # 0: Non, 1: Oui

# Standardisation des variables numériques
scaler = StandardScaler()
df[['Age', 'Revenu']] = scaler.fit_transform(df[['age', 'revenu']])
