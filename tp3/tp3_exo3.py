from time import sleep

n = int(input("Veuillez entrer un nombre N : "))

for i in range(0,n+1):
    print(n-i)
    sleep(1)

while n >= 0:
    print(n)
    n=n-1
    sleep(1)