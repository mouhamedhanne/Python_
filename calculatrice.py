# Etape 1: demander a l'utilisateur d'entrer deux nombre et un symbole
nombre_1 = float(input("Entrer le premier nombre : "))
nombre_2 = float(input("Entrer le deuxieme nombre : "))
operator = input("Entrez le symbole d'operation (+, -, *, /) : ") 

#Etape 1: verifier la valiite des variables et du symbole
if operator not in ["+", "-", "*", "/"]:
    print("Symbole d'operation invalide. Utiliser l'un des suivants : +, -, *, /")
else:
    #Etape 3: Effectuer l'operation en fonction du symbole choisi
    if operator == "+":
        print(f"{nombre_1} + {nombre_2} = {nombre_1 + nombre_2}")
    elif operator == "-":
        print(f"{nombre_1} - {nombre_2} = {nombre_1 - nombre_2}")
    elif operator == "*":
        print(f"{nombre_1} x {nombre_2} = {nombre_1 * nombre_2}")
    elif operator == "/":
        #verifier si le deuxieme nombre n'est pas egal a zero
        if nombre_2 != 0 :
            print(f"{nombre_1} / {nombre_2} = {nombre_1 / nombre_2}")
        else:
            print("Error : Impossible de diviser par zero")
        
