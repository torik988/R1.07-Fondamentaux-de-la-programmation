calendrier_normal = [31,28,31,30,31,30,31,31,30,31,30,31]
calendrier_bisext = [31,29,31,30,31,30,31,31,30,31,30,31]


entree_date = input("Entrez la date au format jjmmaaaa: ")
if len(entree_date) != 8:
    print("La date n'est pas valide")

jour=int(entree_date[0]+entree_date[1])
mois=int(entree_date[2]+entree_date[3])
annee=int(entree_date[4]+entree_date[5]+entree_date[6]+entree_date[7])

if (mois>=1) and (mois<=12):
    if annee%4==0 and annee%100!=0 or annee%400==0:#on verif si c'est une annee bisextile
        if (jour>=1) and (jour <= calendrier_bisext[mois-1]):
            print(entree_date, " (correcte)")

        else:
            print(entree_date, " (incorrecte)")
    else:
        if (jour >= 1) and (jour <= calendrier_normal[mois - 1]):
            print(entree_date, " (correcte)")

        else:
            print(entree_date, " (incorrecte)")
else:
    print(entree_date, " (incorrecte)")




