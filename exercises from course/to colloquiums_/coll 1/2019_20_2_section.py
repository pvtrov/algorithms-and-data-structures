"""
Mamy n żołnierzy różnego wzrostu i nieuporządkowaną tablicę, w której
podano wzrosty żołnierzy. Żołnierze zostaną ustawieni na placu w szeregu malejąco względem
wzrostu. Proszę zaimplementować funkcję:
section(T,p,q)
która zwróci tablicę ze wzrostami żołnierzy na pozycjach od p do q włącznie. Użyty algorytm
powinien być możliwie jak najszybszy. Proszę w rozwiązaniu umieścić 1-2 zdaniowy opis
algorytmu oraz proszę oszacować jego złożoność czasową.
"""
"""
O((p-q)*n)
"""


def partition(array, p, r):
    pivot = array[r]
    i = p-1
    for j in range(p, r):
        if array[j] >= pivot:
            array[j], array[i+1] = array[i+1], array[j]
            i += 1
    array[i+1], array[r] = array[r], array[i+1]
    return i+1


def select(array, p, r, elem):
    if p == r:
        return array[p]
    q = partition(array, p, r)
    if q == elem:
        return array[q]
    elif elem < q:
        return select(array, p, q-1, elem)
    else:
        return select(array, q+1, r, elem)


def section(array, p, q):
    result = []
    for i in range(p, q+1):
        result.append(select(array, 0, len(array)-1, i))

    return result


soldeirs = [188, 198, 176, 180, 201, 189, 175, 180, 169]
print(section(soldeirs, 4, 7))