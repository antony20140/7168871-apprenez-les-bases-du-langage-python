fruits={"pomme":"rouge", "banane":"jaune", "orange":"orange"}
fruits["kiwi"] = "vert"
fruits["couleur_banane"] = "jaune"
fruits=["pomme"]="vert"
del fruits["orange"]
 print(fruits)
{'pomme': 'vert', 'banane': 'jaune', 'pommes': 'vert'}
print(fruits.keys())
dict_keys(['pomme', 'banane', 'pommes'])
