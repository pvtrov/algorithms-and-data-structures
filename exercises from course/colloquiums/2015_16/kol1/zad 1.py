"""1. Proszę zaimplementować funkcję void SumSort(int A[], int B[], int n). Funkcja ta
przyjmuje na wejściu dwie n
2
-elementowe tablice (A i B) i zapisuje w tablicy B taką permutację
elementów z A, że:
nX−1
i=0
B[i] ¬
2
Xn−1
i=n
B[i] ¬ ... ¬
nX2−1
i=n2−n
B[i].
Proszę zaimplementować funkcję SumSort tak, by działała możliwie jak najszybciej. Proszę
oszacować i podać jej złożoność czasową."""

""" by warunki rozwiązania byly spełnione wystarczy posortować tablice, robie to quicksortem, złożonosc to O(nlogn)"""


def partition(T, p, r):
    x = T[r]
    i = p - 1
    for j in range(p, r):
        if T[j] <= x:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i + 1], T[r] = T[r], T[i + 1]
    return i + 1


def no_tail_quicksort(T, p, r):
    while p < r:
        q = partition(T, p, r)

        if (q - p) < (r - q):
            no_tail_quicksort(T, p, q - 1)
            p = q + 1
        else:
            no_tail_quicksort(T, q + 1, r)
            r = q - 1
    return T


def sum_sort(A, n):
    B = no_tail_quicksort(A, 0, (n ** 2) - 1)
    return B


if __name__ == '__main__':
    A = [0, 7, 5, 3, 6, 5, 3, 67, 8]
    n = 3
    print(sum_sort(A, n))
