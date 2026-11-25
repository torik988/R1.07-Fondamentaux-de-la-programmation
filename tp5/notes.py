notes=[]
nm_notes = 5
for i in range(nm_notes):
    notecoef = input(f"Veuillez entrer la note du module {i+1} et le coefficient correspondant : ")
    notes.append(notecoef.split(" "))

moy = 0
somme_coef = 0
print(notes)
for i in notes:
    n = float(i[0])
    coef = float(i[1])

    moy += (n*coef)
    somme_coef += coef

moyenne = round((moy/somme_coef), 2)
print(moyenne)

if moyenne > 8:
    print(f"L'etudiant est admis avec une moyenne de {moyenne}")
else:
    print(f"L'etudiant n'est pas admis, sa moyenne de {moyenne}, donc inferieur a 8")