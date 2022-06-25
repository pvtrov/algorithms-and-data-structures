"""
Zadaniem tej funkcji jest obliczyć sumę liczb z n elementowej tablicy T, które w posortowanej
tablicy znajdywałyby się na pozycjach o indeksach od from do to (włącznie). Można przyjąć, że
liczby w tablicy T są parami różne (ale nie można przyjmować żadnego innego rozkładu danych).
Zaimplementowana funkcja powinna być możliwie jak najszybsza. Proszę oszacować jej złożoność
czasową (oraz bardzo krótko uzasadnić to oszacowanie).
"""

"""
O((from-to) * n)
"""


def partition(array, p, r):
    x = array[r]
    j = p-1
    for i in range(p, r):
        if array[i] <= x:
            j += 1
            array[j], array[i] = array[i], array[j]
    array[j+1], array[r] = array[r], array[j+1]
    return j+1


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


def sum_between(array, from_, to, n):
    sum = 0
    for i in range(from_, to+1):
        sum += select(array, 0, len(array)-1, i)
    return sum



array = [1, 3, 2, 6, 5]
from_ = 1
to = 4
n = 5
print(sum_between(array, from_, to, n))