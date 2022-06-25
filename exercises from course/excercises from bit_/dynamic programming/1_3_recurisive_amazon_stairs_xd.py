"""
Cel: dana jest tablica A zawierająca liczby naturalne nie mniejsze od 1. początkowo stoimy na pozycji 0, wartość A[i]
informuje nas jaka jest maksymalna długość skoku na następną pozycję.

Przykład A = {1,3,2,1,0}
Z pozycji 0 mogę przejść na pozycję 1. z pozycji 1 mogę przejść na 2, 3, 4. Należy policzyć na ile sposobów mogę
przejść z pozycji 0 na pozycję n-1, przestrzegając reguł tablicy.
"""

"""
wykonuje to rekurencyjnie, dla każdej możliwośći. Gdy dobijam do n-1 to zwiekszam licznik o 1
zwracam licznik
"""


def siup(A, i, n, counter):
    if i > n:
        return
    if i == n:
        counter += 1
    max_length = A[i]
    for j in range(1, max_length+1):
        counter = siup(A, i+j, n, counter)
    return counter


def recursive_stairs(A):
    n = len(A)-1
    counter = 0
    counter = siup(A, 0, n, counter)
    return counter


A = [1, 3, 2, 1, 0]
print(recursive_stairs(A))