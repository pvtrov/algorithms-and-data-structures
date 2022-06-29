"""
Kapitan pewnego statku zastanawia się, czy może wpłynąć do portu mimo tego, że nastąpił
odpływ. Do dyspozycji ma mapę zatoki w postaci tablicy:
int n = ...
int m = ...
int A[m][n];
gdzie wartość A[y][x] to głębokość zatoki na pozycji (x, y). Jeśli jest ona większa niż pewna
wartość int T to statek może się tam znaleźć. Początkowo statek jest na pozycji (0, 0) a port
znajduje się na pozycji (n − 1, m − 1). Z danej pozycji statek może przepłynąć bezpośrednio
jedynie na pozycję bezpośrednio obok (to znaczy, na pozycję, której dokładnie jedna ze
współrzędnych różni się o jeden). Proszę napisać funkcję rozwiązującą problem kapitana.
"""
""" cos tu nie dziala ale pomysl jest git, ewentualnie mozna zrobic z tego graf i znalezc czy istnieje sciezka z u do v
"""
moves =[(-1, 0), (0, -1), (1, 0), (0, 1)]


class Field:
    def __init__(self, depth):
        self.depth = depth
        self.parent = None


def is_in_map(n, m, row, column):
    return 0 <= row < m and 0 <= column < n


def sail(map, row, column, int):
    if row == len(map)-1 and column == len(map[0])-1:
        return True

    for move in moves:
        new_row = row + move[0]
        new_column = row + move[1]
        if is_in_map(len(map[0]), len(map), new_row, new_column) \
                and map[new_row][new_column].depth > int \
                and map[new_row][new_column].parent != (row, column):
            map[new_row][new_column].parent = (row, column)
            return sail(map, new_row, new_column, int)
    return


def captain(map, int):
    for i in range(len(map)):
        for j in range(len(map[0])):
            map[i][j] = Field(map[i][j])

    return sail(map, 0, 0, int)


map = [[6, 5, 9, 2, 4],
       [3, 6, 2, 1, 8],
       [5, 1, 0, 2, 3],
       [9, 8, 7, 6, 0],
       [5, 4, 6, 2, 1],
       [7, 9, 8, 2, 5]]
print(captain(map, 1))

