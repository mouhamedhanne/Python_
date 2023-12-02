new_campagne = {"nom": "Campagne de English Mentor AI", "date_begin": "2024-01-01",
 "type": "type 1", "statut": "statut 1"}

print(new_campagne)

avec_soleil = True
en_semaine = False

if avec_soleil and not en_semaine:
    print("On vas a la plage")
elif avec_soleil and en_semaine:
    print("On vas au travail")
else:
    print("On reste a la maison")

animal = "chat"
match animal:
    case "chat":
        print("miaou miaou")
    case "chien":
        print("houhou houhou")
    case "oiseau":
        print("plop plop")
    case _ :
        print("Je ne connais pas cet animal")