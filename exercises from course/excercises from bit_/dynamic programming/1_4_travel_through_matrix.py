"""
Dostajemy tablicę (M x N) wypełnioną wartościami(kosztem wejścia). Mamy znaleźć minimalny koszt potrzebny do dostania
się z pozycji [0][0] do [M-1][N-1]

Wprowadzimy na początek pewne ułatwienia:
1. Możemy poruszać się tylko w bok i w dół
2. Wszystkie koszty są dodatnie
"""


def go_through(matrix, row, column, cost, walk_cost):
    if row >= len(matrix) or column >= len(matrix[0]) or column < 0:
        return float("inf")
    elif row == len(matrix)-1 and column == len(matrix[0])-1:
        return cost + matrix[row][column]

    cost += matrix[row][column]
    if cost >= walk_cost[row][column]:
        return float("inf")
    else:
        walk_cost[row][column] = cost

    return min(go_through(matrix, row + 1, column, cost, walk_cost), go_through(matrix, row, column + 1, cost, walk_cost),
               go_through(matrix, row, column-1, cost, walk_cost))


def travel(matrix):
    walk_cost = [[float("inf") for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    print(walk_cost)
    cost = go_through(matrix, 0, 0, 0, walk_cost)
    return cost


matrix = [[5, 2, 8], [2, 3, 6], [5, 1, 9]]
matrix1 = [[1, 1, 1, 1, 1], [9, 9, 9, 9, 1], [9, 9, 9, 1, 9], [9, 9, 9, 1, 9], [9, 9, 9, 1, 1]]
print(travel(matrix1))