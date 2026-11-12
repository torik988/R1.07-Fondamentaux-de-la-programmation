from random import randint
entree= 101
n, cpt = randint(0,100), 0
while n != entree:
    entree= int(input("Veuillez entrer un nombre : "))
    if entree == n:
        print(f"Bravo, vous avez trouve en {cpt}!!")
    elif entree > n:
        print("Votre prediction est trop grande ")
    elif entree < n:
        print("Votre prediction est trop petite ")
    cpt += 1
