def calcul_salaire_horaire(salaire_mensuel, heure_travail_semaine) :
    heure_travail_mois = heure_travail_semaine * 4
    salaire_horaire = salaire_mensuel / heure_travail_mois
    return salaire_horaire

def main() :
    salaire_mensuel = float(input("Entrez votre salaire mensuel: "))
    heure_travail_semaine = float(input("Entrez votre temps de travail par semaine: "))
    salaire_horaire = calcul_salaire_horaire(salaire_mensuel, heure_travail_semaine)
    
    print(f"votre salaire horaire : {salaire_horaire: .2f} Fcfa par heure")
if __name__ == "__main__" :
    main()