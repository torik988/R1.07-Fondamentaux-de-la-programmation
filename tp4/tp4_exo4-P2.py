L1 = [2, 7, 5, 6, 7, 41, 7, 6, 2, 1, 7, 6]

glo_maxi = 0
glo_val = 0

for i in L1:
    compte=L1.count(i)
    if compte > glo_maxi:
        glo_maxi = compte
        glo_val = i
print(f"Le nombre le plus fréquent dans la liste est le : {glo_val} ({glo_maxi} x) ")