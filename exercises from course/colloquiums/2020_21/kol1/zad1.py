from zad1testy import runtests


def partition(array, p, r):
    pivot = array[r]
    i = p-1
    for j in range(p, r):
        if pivot >= array[j]:
            array[i+1], array[j] = array[j], array[i+1]
            i += 1
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


def Median(T):
    tab = []
    n = len(T)
    for i in range(n):
        tab.extend(T[i])

    for i in range(n):
        elem = (int((n/2)*(n-1)) + i)
        T[i][i] = select(tab, 0, len(tab)-1, elem)

    index = 0
    for i in range(n):
        for j in range(i):
            T[i][j] = tab[index]
            index += 1

    index += n
    for i in range(n):
        for j in range(i+1, n):
            T[i][j] = tab[index]
            index += 1

    return T


runtests( Median )
