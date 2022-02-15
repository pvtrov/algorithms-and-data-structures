"""
Kapitan pewnego statku zastanawia
się, czy może wpłynąć do portu mimo, że nastąpił odpływ. Do dyspozycji ma mapę zatoki w postaci tablicy
M, gdzie M[y][x] to głebokość zatoki na pozycji (x, y). Jeśli jest ona większa niż pewna wartość int T
to statek może się tam znaleźć. Początkowo statek jest na pozycji (0, 0) a port znajduje się na pozycji
(n − 1, m − 1). Z danej pozycji statek może przepłynąć bezpośrednio jedynie na pozycję bezpośrednio obok
(to znaczy, na pozycję, której dokładnie jedna ze współrzędnych różni się o jeden). Proszę napisać funkcję
rozwiązującą problem kapitana.
"""

"""
1. z tablicy tworzymy graf, ilosc wierzcholkow to n * m
2. w kazdym wierzchołku przechowywujemy jego wartość ( glebokosc zatoki w jego miejscu )
3. wierzchołki które byly obok siebie w tablicy łączymy krawedziami
4. sprawdzamy czy można dojść do wierzcholka koncowego, tak by sciezka spełniala załozenia ( nie przechodzi przez
 wierzcholek o mniejszej glebokosci niz zadana liczba T )
"""
from math import inf


class Vertex:
    def __init__(self, index, value):
        self.idx = index
        self.val = value
        self.neigh = []


def searching(vertex, indexes, u, v):
    for i in range(len(indexes)):
        if indexes[i][0] == u and indexes[i][1] == v:
            vertex.append(Vertex(i, matrix[u][v]))


def adding_neighbours(vertex, m, n, i, j, indexes):
    if i == 0:
        if j == 0:
            searching(vertex, indexes, i, j + 1)
            searching(vertex, indexes, i + 1, j)
        elif j == n:
            searching(vertex, indexes, i + 1, j)
            searching(vertex, indexes, i, j - 1)
        else:
            searching(vertex, indexes, i, j - 1)
            searching(vertex, indexes, i + 1, j)
            searching(vertex, indexes, i, j + 1)
    elif i == m:
        if j == n:
            searching(vertex, indexes, i - 1, j)
            searching(vertex, indexes, i, j - 1)
        elif j == 0:
            searching(vertex, indexes, i - 1, j)
            searching(vertex, indexes, i, j + 1)
        else:
            searching(vertex, indexes, i - 1, j)
            searching(vertex, indexes, i, j - 1)
            searching(vertex, indexes, i, j + 1)
    elif j == 0:
        searching(vertex, indexes, i - 1, j)
        searching(vertex, indexes, i + 1, j)
        searching(vertex, indexes, i, j + 1)

    elif j == n:
        searching(vertex, indexes, i - 1, j)
        searching(vertex, indexes, i + 1, j)
        searching(vertex, indexes, i, j - 1)

    else:
        searching(vertex, indexes, i, j - 1)
        searching(vertex, indexes, i, j + 1)
        searching(vertex, indexes, i + 1, j)
        searching(vertex, indexes, i - 1, j)


def find_path(graph, start, end, path, limit):
    path = path + [start]

    if start == end:
        return path

    if len(graph[start].neigh) == 0:
        return None

    new_path = None
    for vertex in graph[start].neigh:
        if vertex.idx not in path and vertex.val > limit:
            new_path = find_path(graph, vertex.idx, end, path, limit)

    return new_path


def create_graph(matrix, m, n):
    graph = [[] for _ in range(m * n)]
    indexes = [[0, 0] for _ in range(m * n)]
    index_counter = 0
    for v in range(m):
        for u in range(n):
            indexes[index_counter][0] = v
            indexes[index_counter][1] = u
            index_counter += 1

    index_counter = 0
    for i in range(m):
        for j in range(n):
            graph[index_counter] = Vertex(index_counter, matrix[i][j])
            adding_neighbours(graph[index_counter].neigh, m, n, i, j, indexes)
            index_counter += 1

    return graph


def if_sailor_can_take_a_trip(matrix, m, n, limit):
    graph = create_graph(matrix, m, n)
    path = find_path(graph, 0, len(graph) - 1, [], limit)

    if path is None or len(path) <= 1:
        return False
    else:
        return True


if __name__ == '__main__':
    matrix = [[0, 5, 6],
              [4, 3, 4],
              [5, 6, inf]]
    print(if_sailor_can_take_a_trip(matrix, 3, 3, 2))
