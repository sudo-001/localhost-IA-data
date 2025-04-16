import pandas as pd

# Chargement des données
df = pd.read_csv("./dataset/donnees_manquantes.csv")

# Affichage initial
print("Données originales :\n", df)

# Détection des valeurs manquantes
print("\nValeurs manquantes par colonne :\n", df.isna().sum())

######### Suppression des lignes contenant des valeurs manquantes
# df_drop = df.dropna()
# print("\nAprès suppression des lignes avec valeurs manquantes :\n", df_drop)

######### Imputation des valeurs manquantes avec une valeur par défaut
# df_default = df.fillna({
#     'note_math': 0,  # Exemple : remplacer les valeurs manquantes par 0
#     'note_physique': 0,
#     'age': df['age'].median()  # Exemple : remplacer par la médiane pour l'âge
# })
# print("\nAprès imputation avec des valeurs par défaut :\n", df_default)


# Imputation des valeurs manquantes par la moyenne
df_mean = df.fillna(df.mean(numeric_only=True))
print("\nAprès imputation par la moyenne :\n", df_mean)

# Imputation par la moyenne (pour les notes)
df_fill = df.copy()
df_fill['note_math'] = df_fill['note_math'].fillna(df_fill['note_math'].mean())
df_fill['note_physique'] = df_fill['note_physique'].fillna(df_fill['note_physique'].mean())
df_fill['age'] = df_fill['age'].fillna(df_fill['age'].median())  # Exemple avec médiane
print("\nAprès imputation :\n", df_fill)
