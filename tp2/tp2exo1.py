x,y = input("x : ") , input("y: ")
print(f"Avant permutation, \nX : {x}, \nY : {y}")

tmp = x
x= y
y = tmp

print(f"Apres permutation, \nX : {x}, \nY : {y}")