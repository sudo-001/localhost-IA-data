import pandas as pd

df = pd.read_csv("./dataset/dataset.csv")


colonne_A = df['Age']
filtre = df[df['Age'] > 30]
