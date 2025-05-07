# 1. Importation des librarires necessaires
import pandas as pd


# 2. Chargement du jeu de donnees
df = pd.read_csv("./dataset/valeurs_aberrantes.csv")

# 3. Selection des colonnes contenant les valeurs categorielle
categorials_columns = df.select_dtypes(include=['object']).columns

# 4. Analyse du nombre d'occurences pour chaque colonne categorielle identifiee
for cat in categorials_columns:
    print("\nCalcul occurence pour chaque colonnes categorielle\n")
    print(df[cat].value_counts())

# 5. Traitement sur la(les) colonnes contenant les variables categorielles

#########################################################
# # Creation du dictionnaire des valeurs correctes (Ferry)
# true_values = {
#     'female': 'F',
#     'Homme': 'M',
#     'féminin': 'F',
#     'F':'F',
#     'masculin': 'M',
#     'homme': 'M',
#     'M': 'M',
#     'male': 'M',
#     'Autre': 'Autre',
#     'Femme': 'F',
#     'femme': 'F',
#     'H': 'M',
#     'FEMME': 'F',
# }
# # On remplace partout dans la colonne 

# df['sexe'] = df['sexe'].replace(true_values)

# print(df['sexe'].value_counts())

#########################################################


######################################################### ( Danielle )

# df['sexe'] = df['sexe'].apply(lambda x:'M' if x in ['Homme', 'masculin','homme','M','male', 'H'] else ('F' if x in ['female','féminin','F','Femme','femme','FEMME'] else x))

# print(df['sexe'].value_counts())

#########################################################



for cat in categorials_columns:
    count_values_var = df[cat].value_counts()
    # rare_values_var = count_values_var[count_values_var < 20].index
    all_values = count_values_var[count_values_var > 0].index
    # print(f"All values {all_values}")
    
    if cat == "sexe":
        for v in all_values:
            print(f'val => {v}')
            
            if v in ['Homme', 'masculin','homme','M','male', 'H'] :
                df[cat] = df[cat].replace({
                    v: 'H'
                })        
            else:
                df[cat] = df[cat].replace({
                v: 'F'
                })
    # print("Values \n")
    # for  val in count_values_var:
    #     print(f'{[val]}')
    # df[cat] = df[cat].replace(rare_values_var, "NEW_US")
    
    
    

# 6. Visualisation du nouveau jeu de donnees
for cat in categorials_columns:
    print("\nCalcul occurence pour chaque colonnes categorielle\n")
    print(df[cat].value_counts())
    
    
# 7. Sauvegarde de la nouvelle version du jeu de donnees en CSV
