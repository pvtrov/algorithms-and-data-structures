"""
Dana jest szachownica A o wymiarach n × n. Szachownica
zawiera liczby wymierne. Należy przejść z pola (1, 1) na pole (n, n) korzystając jedynie z ruchów “w dół”
oraz “w prawo”. Wejście na dane pole kosztuje tyle, co znajdująca się tam liczba. Proszę podać algorytm
znajdujący trasę o minimalnym koszcie
"""
"""
f(matrix, i, j, cost) - minimalny koszt dojscia do i,j tego pola

f(matrix, 0, j, cost) = f(matrix, 0, j-1, cost + matrix[0][j-1])
f(matrix, i, 0, cost) = f(matrix, i, 0, cost + matrix[i-1][0])
f(matrix, 0, 0, cost) = 0
f(matrix, i, j, cost) = min[ f(matrix, i-1, j, cost + matrix[i-1][j])
                             f(matrix, i, j-1, cost + matrix[i][j-1]) ]
"""


def walking(matrix, i, j):
    if i == 0 or j == 0:
        return matrix[0][0]

    return min(walking(matrix, i-1, j), walking(matrix, i, j-1)) + matrix[i-1][j-1]


if __name__ == '__main__':
    matrix = [[5, 3, 2, 1],
              [9, 8, 1, 3],
              [4, 5, 7, 8],
              [1, 0, 3, 7]]
    print(walking(matrix, 3, 3))