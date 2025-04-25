import pandas as pd
import seaborn as sns

df = sns.load_dataset("tips")

print("Statistiques descriptives globales")
# Statistiques descriptives globales
print(df.describe())

print("-------------------------------------------------------------------------------------------")
# Moyenne des pourboires
print("Moyenne des pourboires :", df['tip'].mean())

# Mediane des pourboires
print("Mediane des pourboires :", df['tip'].median())

# Ecart-type des pourboires
print("Ecart-type des pourboires :", df['tip'].std())

# Variance des pourboires
print("Variance des pourboires :", df['tip'].var())

# Coefficient de variation des pourboires
print("Coefficient de variation des pourboires :", df['tip'].std() / df['tip'].mean())

