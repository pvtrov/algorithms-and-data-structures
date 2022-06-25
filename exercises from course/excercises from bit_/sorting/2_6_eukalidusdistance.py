"""
Dane jest n punktów na osi liczbowej jednowymiarowej. Napisz algorytm, który stwierdzi, w którym z nim należy wybudować
dom, tak aby suma euklidesowych odległości od tego punktu do wszystkich pozostałych była minimalna. Należy zwrócić
również tę sumę. Algorytm powinien być jak najszybszy.
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


def select(array, p, r, elem):
    if p == r:
        return array[p]
    q = partition(array, p, r)
    if q == elem:
        return array[q]
    elif q < elem:
        return select(array, q+1, r, elem)
    else:
        return select(array, p, q-1, elem)


def count_diff(array, x):
    sum = 0
    for i in range(len(array)):
        sum += abs(x - array[i])

    return sum


def eukalid_diff(array):
    if len(array) % 2 != 0:
        return array[select(array, 0, len(array)-1, len(array)//2)]
    else:
        return min(count_diff(array, array[select(array, 0, len(array)-1, len(array)//2)]),
            count_diff(array, select(array, 0, len(array)-1, len(array)//2 - 1)))




array = [1, 2, 3,4 ,5, 6]
print(eukalid_diff(array))