nb = int(input("Entrer un nombre entier : "))
typ, la_pari = "",""
if nb > 0:
    typ="Positif"
else:
    typ="Negatif"
if nb%2==0:
    la_pari="Pair"
else:
    la_pari="Impair"
if nb == 0:
    print("Le nombre est zéro (et il est pair)")
else:
    print("C'est un nombre {} et {}.".format(typ,la_pari))