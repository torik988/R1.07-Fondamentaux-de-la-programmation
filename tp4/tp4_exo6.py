def tri_selection(tableau):
    n = len(tableau)
    for i in range(n):
        minimum = i
        print(tableau)
        for j in range(i + 1, n):
            if tableau[j] < tableau[minimum]:
                minimum = j
        tableau[i] = tableau[minimum]
        tableau[minimum] = tableau[i]

    return tableau

tab=[5, 2, 4, 8, 1, 3]

tri_selection(tab)
"""
2 la fonction sorted trie automatiquement dans python un tableau
3 cela nous renvoie none, aucune info disponible
"""