while True:
    debut = int(input("Donnez l’heure de début de la location (un entier) : "))
    fin = int(input("Donnez l’heure de fin de la location (un entier) : "))
    nb_h_creuse=0
    nb_h_pleine=0
    prix_loc = 0
    #1 Calcul des nb d'heures par categorie:
    if fin>debut:
        for i in range(debut, fin):
            if (i >= 0 and i < 7) or (i >= 17 and i < 24):
                nb_h_creuse+=1
            elif (i >=7 and i < 17):
                nb_h_pleine+=1
        if nb_h_pleine == 0:
            print(f"Vous avez loue votre velo pendant \n{nb_h_creuse} heure(s) au tarif horaire de 1.0 euro(s)")
        elif nb_h_creuse == 0:
            print (f"Vous avez loue votre velo pendant \n{nb_h_pleine} heure(s) au tarif horaire de 2.0 euro(s)")
        else:
            print(f"Vous avez loue votre velo pendant \n{nb_h_creuse} heure(s) au tarif horaire de 1.0 euro(s)")
            print(f"{nb_h_pleine} heure(s) au tarif horaire de 2.0 euro(s)")


        prix_loc = nb_h_creuse*1 + nb_h_pleine*2
        print(f"Le montant total a payer est de {prix_loc} euro(s)")

    elif debut<fin:
        print("l'heure de debut doit etre inferieur a l'heure de fin !")
    else:
        print("L'heure de debut et l'heure de fin sont identiques")