# Proszę zaimplementować algorytm QuickSort do sortowania n elementowej tablicy tak, żeby
# zawsze używał najwyżej O(log n) dodatkowej pamięci na stosie, niezależnie od jakości podziałów w funkcji
# partition.

def partition(array, p, r):
    x = array[r]
    i = p - 1
    for j in range(p, r):
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[r] = array[r], array[i + 1]
    return i + 1


def quicksort_z_zad1(array, p, r):
    while p < r:
        q = partition(array, p, r)

        if (q - p) < (r - q):
            quicksort_z_zad1(array, p, q - 1)
            p = q + 1
        else:
            quicksort_z_zad1(array, q + 1, r)
            r = q - 1
    return array
