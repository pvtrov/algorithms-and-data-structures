"""Proszę zaimplementować funkcję:
int SumBetween(int T[], int from, int to, int n);
Zadaniem tej funkcji jest obliczyć sumę liczb z n elementowej tablicy T, które w posortowanej
tablicy znajdywałyby się na pozycjach o indeksach od from do to (włącznie). Można przyjąć, że
liczby w tablicy T są parami różne (ale nie można przyjmować żadnego innego rozkładu danych).
Zaimplementowana funkcja powinna być możliwie jak najszybsza. Proszę oszacować jej złożoność
czasową (oraz bardzo krótko uzasadnić to oszacowanie)."""

""" w tym zadaniu korzystam z statystyk pozycyjnych, ( to - from ) razy puszczam funkcje select (wyznaczajacą element 
znajdujący sie na x miejscu ) i dodaje do siebie to co ta funkcja zwróci. Złożoność tej funkcji to O[( to - from ) * n].
"""


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


def SumBetween(T, start, to, lenghtOfArray):
    k = start
    sum = 0
    while k <= to:
        sum += select(T, 0, lenghtOfArray, k)
        k += 1
    return sum

if __name__ == '__main__':
    T = [8, 9 ,2, 0, 10, 15, 5, 6]
    n = 7
    print(SumBetween(T, 4, 6, 7))
