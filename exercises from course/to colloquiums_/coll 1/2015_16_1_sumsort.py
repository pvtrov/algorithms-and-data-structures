"""
Proszę zaimplementować funkcję void SumSort(int A[], int B[], int n). Funkcja ta
przyjmuje na wejściu dwie n
2
-elementowe tablice (A i B) i zapisuje w tablicy B taką permutację
elementów z A, że:

Proszę zaimplementować funkcję SumSort tak, by działała możliwie jak najszybciej. Proszę
oszacować i podać jej złożoność czasową.
"""

"""
uzywam sobie selecta zeby nie musiec przechodzic jeszcze raz po tablicyy a po tym jak ja posortuje
"""


def partition(array, p, r):
    x = array[r]
    i = p - 1
    for j in range(p, r):
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[r] = array[r], array[i + 1]
    return i + 1


def select(array, p, r, elem):
    if p == r:
        return array[p]

    q = partition(array, p, r)
    if elem == q:
        return array[q]

    elif elem > q:
        return select(array, q + 1, r, elem)
    else:
        return select(array, p, q - 1, elem)


def sumSort(A, n):
    for i in range(n, n * n, n):
        select(A, i-n, len(A) - 1,  n)
    return A



A = [5, 6, 7, 1, 3, 23, 56, 12, 4, 67, 23, 5, 0, 2, 18, 19]
print(sumSort(A, 4))