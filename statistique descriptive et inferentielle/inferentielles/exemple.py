import seaborn as sns
from scipy.stats import ttest_ind

df = sns.load_dataset("tips")

# Separation des groupes
male_tips = df[df['sex'] == 'Male']['tip']
female_tips = df[df['sex'] == 'Female']['tip']

# Test t de student
stat, p_value = ttest_ind(male_tips, female_tips)

# Affichage des resultats
print("Statistique t :", stat)
print("Valeur p :", p_value)

if p_value < 0.05:
    print("Difference significative entre les pourboires des hommes et des femmes")
else:
    print("Pas de difference significative entre les pourboires des hommes et des femmes")