"""
Dostajemy tablicę (M x N) wypełnioną wartościami. Mamy za zadanie znaleźć najdłuższą ścieżkę w tej tablicy
(możemy przechodzić na pola sąsiadujące krawędziami), o rosnących wartościach (to znaczy, że z pola o wartości 3, mogę
przejść na pola o wartości większej bądź równej 4).

Na początku wprowadzimy ponownie pewne ułatwienie:
Mamy dany punkt początkowy
"""


def find_path(matrix, row, column, prev_value, length):
    if row >= len(matrix) or column >= len(matrix[0]) or column < 0 or row < 0:
        return length

    if prev_value >= matrix[row][column]:
        return length

    length += 1

    return max(find_path(matrix, row + 1, column, matrix[row][column], length),
               find_path(matrix, row - 1, column, matrix[row][column], length),
               find_path(matrix, row, column + 1, matrix[row][column], length),
               find_path(matrix, row, column - 1, matrix[row][column], length))


def increasing(matrix):
    return find_path(matrix, 0, 0, -1, 0)


matrix = [[5, 6, 7, 8],
          [3, 5, 6, 2],
          [2, 0, 8, 9],
          [2, 4, 5, 1],
          [2, 1, 1, 0]]
print(increasing(matrix))