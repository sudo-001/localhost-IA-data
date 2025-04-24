import pandas as pd

df = pd.read_csv("./dataset/dataset.csv")

#  Ajouter une colonne
df['Nouvelle_Colonne'] = df['Age'] * 2

# Supprimer une colonne
df = df.drop(columns=['Nouvelle_Colonne'])

# Renommer une colonne
df = df.rename(columns={'Nom': 'Prenom'})

# Renommer plusieurs colonnes
df = df.rename(columns={
    'Prenom': 'New Nom',
    'Age': 'New Age'
})
