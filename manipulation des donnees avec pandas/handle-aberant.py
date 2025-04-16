import pandas as pd

# Chargement des données
df = pd.read_csv("./dataset/donnees_aberrantes.csv")

# Affichage initial
print("Données originales :\n", df)

# Détection des valeurs aberrantes par IQR (Interquartile Range)
Q1 = df['temperature'].quantile(0.25)
Q3 = df['temperature'].quantile(0.75)
IQR = Q3 - Q1
borne_inf = Q1 - 1.5 * IQR
borne_sup = Q3 + 1.5 * IQR

# Filtrage des valeurs normales
df_clean = df[(df['temperature'] >= borne_inf) & (df['temperature'] <= borne_sup)]
print("\nTempératures normales (sans aberrations) :\n", df_clean)

# Localiser les villes avec températures aberrantes
df_aberrantes = df[(df['temperature'] < borne_inf) | (df['temperature'] > borne_sup)]
print("\nValeurs aberrantes détectées :\n", df_aberrantes)
