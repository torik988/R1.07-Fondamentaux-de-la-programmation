n=int(input("Veuillez entrer un nombre pour calculer sa factorielle : "))
boucle = str(input("Veuillez saisir le type de boucle : For / While [F/W]"))
nb=1
if boucle == "F":
    for i in range(1,n+1):
        nb=nb*i
        print(nb)
    print()

elif boucle == "W":
    i = n
    while i > 0:
        print(nb)
        nb =nb*i

        i = i - 1
else:
    print("TYPE DE BOUCLE INVALIDE !")
