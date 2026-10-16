def calcul_somme_n_for(n):
    somme = 0
    for i in range(0,n+1):
        somme += i
    return somme

def calcul_somme_n_while(n):
    somme= n
    while n > 0:
        n = n-1
        somme += n
    return somme

def att():
    rep = True
    while rep:
        if input(">") == "100":
            rep = False

def lecture():
    entrees=[]
    val_inf_s_10, val_sup_ou_egal_10_et_inf_s_15, val_sup_ou_egal_15 = 0, 0, 0
    while len(entrees)<=10:
        x=int(input("valeurs réelles comprises entre 0 et 20: "))
        if x<0 or x>20:
            print("Valeur Invalide, veuillez recommencer !!")
        else:
            entrees.append(x)
    for e in entrees:
        if e < 10:
            val_inf_s_10+=1
        if e >= 10 and e < 15:
            val_sup_ou_egal_10_et_inf_s_15+=1
        if e >= 15:
            val_sup_ou_egal_15+=1
    print(f"Le nombre de valeurs inférieur strictement à 10 est de {val_inf_s_10}\nLe nombre de valeurs supérieur ou égale à 10 et inférieur strictement à 15 est de {val_sup_ou_egal_10_et_inf_s_15}\nLe nombre de valeurs supérieur ou égale à 15 {val_sup_ou_egal_15}")

def affichage_plus_grand_N():
    somme = 0
    cpt = 0
    x=0
    while x < 1:
        x = int(input("Donnez une valeur supérieur a 1 :>"))
        if x < 1:
            print("Valeur Invalide, veuillez recommencer !!")
    while somme < x:
        cpt += 1
        somme += cpt
    print(f"Le plus grand nombre n est : {cpt}")
    return cpt

#print(calcul_somme_n_for(int(input("nombre : "))))
#print(calcul_somme_n_while(int(input("nombre : "))))
#att()
#lecture()
affichage_plus_grand_N()