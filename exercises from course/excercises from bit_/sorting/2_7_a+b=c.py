"""
Dane są trzy zbiory reprezentowane przez tablice: A, B i C. Napisz algorytm, który powie, czy istnieje taka trójka
a, b, c z odpowiednio A, B, i C, że a + b = c.  Nie wolno korzystać ze słowników!
"""


def partition(array, p, r):
    pivot = array[r]
    i = p-1
    for j in range(p, r):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[r] = array[r], array[i+1]
    return i+1


def quicksort(array, p, r):
    if p < r:
        q = partition(array, p, r)
        quicksort(array, q+1, r)
        quicksort(array, p, q-1)


def find_sum(A, B, C):
    quicksort(A, 0, len(A)-1)
    quicksort(B, 0, len(B)-1)

    for i in range(len(C)):
        a = 0
        b = len(B)-1
        elem = C[i]
        while a < len(A) and b >= 0:
            if A[a] + B[b] == elem:
                return True
            elif A[a] + B[b] > elem:
                b -= 1
            else:
                a += 1
    return False


A = [6, 10, 6, 4, 7, 20, 15, 10, 20, 11]
B = [10, 5, 9, 7, 6, 7, 20, 8]
C = [1, 2, 3, 3, 4, 1, 1, 3, 4]
print(find_sum(A, B, C))

