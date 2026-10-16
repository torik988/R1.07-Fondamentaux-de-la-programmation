# I =
# [2,3[
#not(x < 2) and x < 4
# ]0,1]
# x < 1 and not(x < -1)
# [-10,-2]
# not(x < -10 or not(x < -2))

# (not(x < 2) and x < 4) or (x < 1 and not(x < -1)) or (not(x < -10 or not(x < -2)))
while True:
    x = int(input("Veuillez entrer un reel :"))
    if not(x < 2) and x < 4:
        print("x appartient à I")
    if x <= 1 and not(x <= 0):
        print("x appartient à I")
    if not(x < -10 or not(x < -2)):
        print("x appartient à I")
    else:
        print("x n'appartient pas à I")