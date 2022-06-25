# Dana jest posortowana tablica A[1...n] oraz liczba x.
# Proszę napisać program, który stwierdza czy istnieją indeksy i oraz j takie, że A[i] + A[j] = x

#
# def suming(array, x):  # o(n^2)
#     for i in range(len(array)):
#         for j in range(len(array)):
#             if array[i] + array[j] == x and i != j:
#                 return i, j
#
#     return "brak indeksów"
#
#
# if __name__ == '__main__':
#     # array = [1, 3, 5, 9, 10, 12]
#     array = [1, 3, 3, 7, 9]
#     print(suming(array, 14))

from math import inf
import sys


def minimumCost(grid, i, j):
    if (i < 0 or j < 0):
        return sys.maxsize
    elif i == 3 or j == 3:
        return grid[i][j]
    else:
        return grid[i][j] + min(minimumCost(grid, i + 1, j + 1), minimumCost(grid, i + 1, j - 1), minimumCost(grid, i + 1, j))


def maxCoins(grid):
    return min(minimumCost(grid, 0, 0), minimumCost(grid, 0, 1), minimumCost(grid, 0, 2), minimumCost(grid, 0, 3))


grid = [[4, 6, 14, 21],
        [17, 0, 5, 5],
        [4, 41, 22, 3],
        [2, 51, 6, 0]]
print(maxCoins(grid))
