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

from time import sleep

for i in range(1, 101) :
    #print(f"chargement {i}%")
    sleep(0.02)
    
for i in range(10):
    if i == 5:
        break
    #print(i)
    
numbers = [1,2,3,4,5]

for element in numbers:
    if element == 3:
        continue
    #print(element)
    
def afficher_msg(prenom, nom) :
    print("Prenom:", prenom)
    print("Nom", nom)

afficher_msg("Mouhamed", "Hanne")

def addition(a, b) :
    resultat = a + b
    #print(resultat)

addition(23, 22)

def soustrac_somme(c, d) :
    result = c - d
    return result

#print(soustrac_somme(23, 22))

numeateur = input("Entrez le numerateur: ")
denominateur = input("Entrez le denominateur: ")

try:
    resultate = int(numeateur) / int(denominateur)
    print(f"le resultat est: {resultate}")
except ZeroDivisionError:
    print("Impossible de diviser par zero")
except ValueError:
    print("Veuillez entrer un nombre")


    
