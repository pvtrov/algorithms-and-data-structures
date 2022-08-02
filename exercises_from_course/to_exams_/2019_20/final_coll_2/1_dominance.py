"""
Mówimy, że punkt (x, y) słabo dominuje punkt (x', y′) jeśli x ≤ x′ oraz y ≤ y′ (w szczególności każdy punkt słabo
dominuje samego siebie). Dana jest tablica P zawierająca n punktów. Proszę zaimplementować funkcję dominance(P),
która zwraca tablicę S taką, że:

1. elementami S są indeksy punktów z P,
2. dla każdego punktu z P, S zawiera indeks punktu, który go słabo dominuje,
3. S zawiera minimalną liczbę elementów.

Przykład. Dla tablicy:
P = [ (2,2), (1,1), (2.5,0.5), (3,2), (0.5,3) ]
# 0 1 2 3 4
wynikiem jest, między innymi:
S = [ 1, 4, 2 ]
"""
"""
sortuje sobie i sprawdzam po kolei czy i jest zdominowane przez poprzednia, jesli tak to przepisuje index z poprzedniej,
(zaujwazmy ze z relacji przechodnosci x <= y i y <= z to x <= z) jak nie to i donminuje samo siebie, taki sprtynty dynamiczek XD
"""


def dominance(P):
    for i in range(len(P)):
        P[i].append(i)
    P.sort()
    domintaing_indexes = [-1] * len(P)
    domintaing_indexes[0] = P[0][2]  # najmnijeszy dominuje sam siebie
    last_x = P[0][0]
    last_y = P[0][1]

    for i in range(1, len(P)):
        if last_x <= P[i][0] and last_y <= P[i][1]:
            domintaing_indexes[i] = domintaing_indexes[i - 1]
        else:
            domintaing_indexes[i] = P[i][2]
        last_x = P[i][0]
        last_y = P[i][1]

    S = set()
    for i in range(len(domintaing_indexes)):
        S.add(domintaing_indexes[i])

    return list(S)


P = [[2, 2], [1, 1], [2.5, 0.5], [3, 2], [0.5, 3]]
print(dominance(P))
