binome = (input("etu 1 :"), input("etu 2 :"))
print(f"L'etudiant {binome[0]} est en binome avec l'etudiant {binome[1]} ")

print("on change le 2 emem pour pedro")
del(binome[1])
print("on change le 2 emem pour pedro")

"""
2 il est impossible de modifier une valeur d'un tuple
3 il est impossible de suprimer une valeur d'un tuple
4 nous devons creer un nouveau tuple avec les premieres valeurs et la nouvelles.
les tuplet sont inaltérable et non modifiable, parfait pour stoquer des infos sensibles a ne pas modifier
"""