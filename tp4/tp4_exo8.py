dico1 = {"name":"toto","firstname":"titi","promo":2026,"group":202}
dico2 = {"name":"tata","firstname":"tutu","promo":2024,"group":102}



######################################################

print(f"votre nom est {dico1['name']}, prénom est {dico1['firstname']}, vous faites partie de la promo {dico1['promo']} et votre groupe est {dico1['group']} ")

######################################################
print("Les cles du dico sont :")
for cle in dico1.keys():
    print("- ",cle)

print("Les valeurs du dico sont :")
for val in dico1.values():
    print("- ",val)

print("Les tuplets du dico sont :")
for item in dico1.items():
    print("- ",item)
######################################################

binome = {"100":dico1,"200":dico2}

print("Les etudiants formant binome sont :")
for item in binome.values():
    print(f"- L'etudiant {item['name']} {item['firstname']} du groupe {item['group']}")



