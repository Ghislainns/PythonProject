#Use a dictionary to store information about a person you know. 


samuel = {}

samuel['prenom'] = "samuel"
samuel['nom'] = "ghislain"
samuel['age'] = 3
samuel['poid'] = 15
samuel['taille'] = 110
samuel['domicile'] = 'incourt'

for key, value in samuel.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
