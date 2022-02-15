# Proszę zaimplementować algorytm znajdowania k-go co do wielkości elementu w tablicy n elementowej w
# “spodziewanym” czasie O(n) na podstawie randomizowanego Partition z QuickSort’a


def partition(T, p, r):
    x = T[r]
    i = p - 1
    for j in range(p, r):
        if T[j] <= x:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i + 1], T[r] = T[r], T[i + 1]
    return i + 1


def select(A, p, r, k):  # statystyki pozycyjne
    if p == r:
        return A[p]
    q = partition(A, p, r)
    if q == k:
        return A[q]
    elif k < q:
        return select(A, p, q - 1, k)
    else:
        return select(A, q + 1, r, k)
