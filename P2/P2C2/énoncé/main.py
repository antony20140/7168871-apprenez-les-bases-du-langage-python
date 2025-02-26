nombres = "1, 2, 3, 4 "
liste = nombres.split (",")
print(liste)
liste = [x.strip() for x in nombres.split(",")]
print(liste)
liste_entiers = []
for nombre in liste:
    nombre_entier = int(nombre)
    liste_entiers.append(nombre_entier)
print("listes des entiers :", liste_entiers)
somme = 0
for nombre in liste_entiers:
    somme += nombre
print("somme des nombres:", somme)
somme = 0
for nombre in liste_entiers:
    somme += nombre
    nombre_elements = len(liste_entiers)
    moyenne = somme / nombre_elements
print("moyenne des nombres:", moyenne)
nombre_sup_moyenne = 0
for nombre in liste_entiers:
    if nombre > moyenne:
        nombre_sup_moyenne += 1
print("Nombre de nombres supérieurs à la moyenne:", nombre_sup_moyenne)# Ecrivez votre code ici !
