l = [[input('Nom1 :').lower(),input('Prenom1 :').lower()],[input('Nom2 :').lower(),input('Prenom2 :').lower()]]

if l[1][0] < l[0][0]:
    l.append(l.pop(0))

if l[1][0] == l[0][0]:
    if l[1][1] < l[0][1]:
        l.append(l.pop(0))

    if l[1][1] == l[0][0]:
        print('Les Noms et Prenoms sont identiques !!!')


for i in range(2):
    personne = l.pop(0)
    print(personne[1].capitalize(), personne[0].upper())