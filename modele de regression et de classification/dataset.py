# Regénération après reset de l'environnement

import pandas as pd
import numpy as np
import random

# Définition de listes de valeurs possibles
noms = [f"Personne_{i}" for i in range(1, 201)]
professions = ['Médecin', 'Ingénieur', 'Enseignant', 'Commerçant', 'Artiste', 'Étudiant', 'Développeur', 'Avocat']
genres = ['Homme', 'Femme', 'Autre']
achats = ['Oui', 'Non']

# Génération du dataset
data = {
    'nom': noms,
    'age': np.random.randint(18, 65, size=200),
    'profession': [random.choice(professions) for _ in range(200)],
    'revenu': [round(random.uniform(100000, 3000000), 2) for _ in range(200)],
    'genre': [random.choice(genres) for _ in range(200)],
    'achat': [random.choice(achats) for _ in range(200)]
}

df = pd.DataFrame(data)

# Sauvegarde en CSV
csv_path = "./dataset/dataset.csv"
df.to_csv(csv_path, index=False)
csv_path
