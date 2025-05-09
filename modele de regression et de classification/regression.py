import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

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

df['Genre'] = LabelEncoder().fit_transform(df['Genre'])  # 0, 1, 2
df['Profession'] = LabelEncoder().fit_transform(df['profession'])
df['Achat'] = LabelEncoder().fit_transform(df['achat'])  # 0: Non, 1: Oui

# Sauvegarder la colonne d'origine du revenu
revenu_original = df['revenu'].copy()

# Standardisation séparée pour l'âge et le revenu
scaler_age = StandardScaler()
scaler_revenu = StandardScaler()

df['Age'] = scaler_age.fit_transform(df[['age']])
df['Revenu'] = scaler_revenu.fit_transform(df[['revenu']])

################################### RÉGRESSION PART ###################################

# Variables explicatives et cible
X = df[['Age', 'Profession', 'Genre']]
y = df['Revenu']  # standardisé

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modèle
reg = LinearRegression()
reg.fit(X_train, y_train)
y_pred = reg.predict(X_test)

# ➤ Déstandardisation (revenir aux CFA)
y_pred_real = scaler_revenu.inverse_transform(y_pred.reshape(-1, 1)).flatten()
y_test_real = scaler_revenu.inverse_transform(y_test.values.reshape(-1, 1)).flatten()

# Enregistrement des prédictions réelles dans un CSV
predictions_df = pd.DataFrame({
    'Revenu Réel': y_test_real,
    'Revenu Prédit': y_pred_real
})
predictions_df.to_csv('./predictions_regression.csv', index=False)

# Évaluation sur valeurs réelles
mae = mean_absolute_error(y_test_real, y_pred_real)
mse = mean_squared_error(y_test_real, y_pred_real)
rmse = np.sqrt(mse)
r2 = r2_score(y_test_real, y_pred_real)

# Affichage
print("Régression - Prédiction du revenu")
print(f"MAE  : {mae:,.0f}")
print(f"MSE  : {mse:,.0f}")
print(f"RMSE : {rmse:,.0f}")
print(f"R²   : {r2:.3f}")
