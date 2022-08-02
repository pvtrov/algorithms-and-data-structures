"""
Dostajemy listę wartości. Gramy z drugim graczem. Wybieramy zawsze jedną wartość z jednego z końców tablicy i
dodajemy do swojej sumy, a następnie to samo robi nasz przeciwnik. Zakładając, że przeciwnik gra optymalnie,
jaką maksymalną sumę możemy uzbierać?
“Uogólniony problem paczki mentosów”
"""
"""
f(i, j) = maksymalna wartosc ktora gracz moze uzyskac of i-tej do j-tej monety

f(i, j) =  max(Vi + min(f(i+2, j), f(i+1, j-1)), Vj + min(f(i+1, j-1), f(i, i-2))
ale:

f(i, j) = Vi, i == j
f(i, j) = max(Vi, Vj), j == i+1

"""


def choose_your_fighter(array, n):
    table = [[0 for _ in range(n)] for _ in range(n)]

    for gap in range(n):
        for j in range(gap, n):
            i = j - gap
            x = 0
            if i + 2 <= j:
                x = table[i + 2][j]
            y = 0
            if i + 1 <= j - 1:
                y = table[i + 1][j - 1]
            z = 0
            if i <= j - 2:
                z = table[i][j - 2]
            table[i][j] = max(array[i] + min(x, y), array[j] + min(y, z))
    return table[0][n - 1]


array = [20, 30, 2, 2, 2, 10]
print(choose_your_fighter(array, len(array)))
