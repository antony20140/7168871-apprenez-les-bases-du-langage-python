#def salaire_mensuel(salaire_annuel):
    return salaire_annuel /12

def salaire_hebdomadaire(salaire_mensuel):
    return salaire_mensuel / 4

def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
    return salaire_hebdomadaire / heures_travaillees

salaire_annuel = 38000

heures_travaillees = 35

mensuel = salaire_mensuel(salaire_annuel)
hebdomadaire = salaire_hebdomadaire(mensuel)
horaire = salaire_horaire(hebdomadaire, heures_travaillees)

print("votre salaire horaire est de ", horaire, "euros") Ecrivez votre code ici
