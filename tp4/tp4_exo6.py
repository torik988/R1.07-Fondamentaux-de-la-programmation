from os import rename

liste= [5, 2, 4, 8, 1, 3]
def sorted(tab):
    pos_mini = 0
    pos_maxi = 0
    nb_element = 0
    for i in liste:#trouve le mini et le maxi de la liste
        nb_element += 1
        if i>liste[pos_mini]:#trouve la position du mini
            pos_mini = i-1
        if i<liste[pos_maxi]:#trouve la position du maxi
            pos_maxi=i-1

    for i in range(nb_element):
        liste[i] = liste.pop(pos_mini)


print(sorted(liste))