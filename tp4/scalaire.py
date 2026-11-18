nMax=5
v1, v2 = [], []
n=0
while not((n>=1) and (n<=nMax)):
    n = int(input("Votre nombre n : "))

print("Saisie du premier vecteur : ")
for i in range(0,nMax):
    nombre= int(input(f"v1[{i}] = "))
    v1.append(nombre)


print("Saisie du second vecteur : ")
for i in range(0,nMax):
    nombre= int(input(f"v2[{i}] = "))
    v2.append(nombre)

scalaire=0
for i in range(0,nMax):
    scalaire=scalaire+v1[i]*v2[i]

print(f"Le produit scalaire de v1 par v2 vaut {scalaire}")