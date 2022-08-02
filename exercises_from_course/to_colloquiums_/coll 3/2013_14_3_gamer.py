"""
Dana jest tablica:
int n = ...
int m = ...
bool A[m][n];
Gracz początkowo znajduje się na (zadanej) pozycji (x, y), dla której zachodzi A[y][x] == true.
Z danej pozycji wolno bezpośrednio przejść jedynie na pozycję, której dokładnie jedna
współrzędna różni się o 1, oraz której wartość w tablicy A wynosi true. Proszę napisać program
obliczający do ilu różnych pozycji może dojść gracz startując z zadanej pozycji (x, y).
"""
moves = [[0, -1], [-1, 0], [1, 0], [0, 1]]


def is_in_map(n, m, row, column):
    return 0 <= row < m and 0 <= column < n


def count_true(board, row, column, counter):
    board[row][column] = 0
    counter = 1

    for move in moves:
        if is_in_map(len(board[0]), len(board), row + move[0], column + move[1]) and board[row + move[0]][column + move[1]] == 1:
            counter += count_true(board, row + move[0], column + move[1], 0)
# czemu counter sie nie zapisuje
    return counter


def gamer(board, row, column):
    counter = 0
    return count_true(board, row, column, counter)
    # return counter


board =[[1, 1, 1, 0],
        [0, 1, 1, 1],
        [0, 1, 0, 1],
        [0, 0, 0, 1]]
print(gamer(board, 0, 0))