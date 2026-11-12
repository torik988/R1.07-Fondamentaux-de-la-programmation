nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0
notes = []
numero_etu = 0
while len(notes) != nombreEtudiants:
    note = float(input(f"Note etudiant N{numero_etu} : "))
    if note > 20 or note < 0:
        print("Note etudiant n'est pas valide")
    else:
        numero_etu = numero_etu + 1
        notes.append([numero_etu, note])
        moyenne += note


moyenne = moyenne / nombreEtudiants

print("Moyenne de classe: ", moyenne)

print("Numero de lEtudiant | note | ecart a la moyenne")
for i in notes:
    print(f"{i[0]} | {i[1]} | {i[1] - moyenne}")