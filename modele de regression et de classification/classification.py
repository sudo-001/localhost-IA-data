import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


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

################################### Classification PART ###################################

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report

# Variables explicatives et cible
X = df[['Age', 'Profession', 'Achat']]  # on ne met pas "Genre" ici car c’est la cible
y = df['Genre']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modèle
clf = LogisticRegression()
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

# Enregistrement des prédictions dans un fichier CSV
predictions_df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
predictions_df.to_csv('./predictions_classification.csv', index=False)

# Évaluation
print("\nClassification - Prédiction du genre")
print(f"Accuracy  : {accuracy_score(y_test, y_pred):.2f}")
print(f"Precision : {precision_score(y_test, y_pred, average='macro', zero_division=0):.2f}")
print(f"Recall    : {recall_score(y_test, y_pred, average='macro', zero_division=0):.2f}")
print(f"F1-score  : {f1_score(y_test, y_pred, average='macro', zero_division=0):.2f}")
print("\nRapport de classification :\n", classification_report(y_test, y_pred, zero_division=0))

