nombre1 = input("Entrez un premier nombre : ")
nombre2 = input("Entrez un deuxième nombre : ")

# Vérifier que ce sont bien des nombres
if not nombre1.isnumeric() or not nombre2.isnumeric():
    print("Erreur : les deux valeurs doivent être des nombres entiers.")
    raise SystemExit("Fin du programme")

# Convertir en entier
nombre1 = int(nombre1)
nombre2 = int(nombre2)

# Demander l'opération
operation = input("Entrez une opération (+, -, *, /) : ")

# Vérifier que l'opération est valide
if operation not in ["+", "-", "*", "/"]:
    print('Erreur : le symbole d\'opération doit être "+", "-", "*" ou "/".')
    raise SystemExit("Fin du programme")

# Calculer le résultat
if operation == "+":
    resultat = nombre1 + nombre2
elif operation == "-":
    resultat = nombre1 - nombre2
elif operation == "*":
    resultat = nombre1 * nombre2
elif operation == "/":
    if nombre2 == 0:
        print("Erreur : impossible de diviser par zéro.")
        raise SystemExit("Fin du programme")
    resultat = round(nombre1 / nombre2, 2)

# Afficher le résultat
print(f"Le résultat de l'opération est : {resultat}")
