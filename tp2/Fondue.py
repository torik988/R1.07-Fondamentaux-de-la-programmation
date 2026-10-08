BASE= 4 #Nb personnes recette
fromage=800.0 #qté fromage /personne
eau=2 #qté eau /personne
ail=2 #qté /personne
pain=400 #qté /personne

convives= int(input("entrer le nombre de convives: "))

print("Pour faire une fondue fribourgeoise pour 3 personnes, il vous faut :")
print(f"- {fromage * convives / BASE} gr de fromage")
print(f"- {eau * convives / BASE} dl d'eau")
print(f"- {ail * convives / BASE} gousse(s) d'ail")
print(f"- {pain * convives / BASE} gr de pain")

