L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

glo_maxi = 0
glo_val = 0

for i in L1:
    maxi = 0
    for j in L1:
        if j == i:
            maxi = maxi + 1
    #verif si c'est le plus grand
    if maxi > glo_maxi:
        glo_maxi = maxi
        glo_val = i

print(f"Le nombre le plus fréquent dans la liste est le : {glo_val} ({glo_maxi} x) ")