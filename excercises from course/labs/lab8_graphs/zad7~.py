# Dana jest szachownica o wymiarach n × n. Każde pole (i, j)
# ma koszt (liczbę ze zbioru {1, . . . , 5}) umieszczony w tablicy A (na polu A[j][i]). W lewym górnym rogu
# szachownicy stoi król, którego zadaniem jest przejsc do prawego dolnego rogu, przechodzac po polach o
# minmalnym sumarycznym koszcie. Prosze zaimplementowac funkcje kings path(A), która oblicza koszt
# sciezki króla. Funkcja powinna byc mozliwie jak najszybsza.

from queue import PriorityQueue
from math import inf

"""
postempujemy analogicznie jak w zadaniu z kapitanem
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


def find_path(graph, start, end, path, limit, minimum):
    path = path + [start]
    limit += graph[start].val

    if start == end:
        return path, minimum

    if len(graph[start].neigh) == 0:
        return None

    shortest = None
    for vertex in graph[start].neigh:
        if vertex.idx not in path:
            new_path, minimum = find_path(graph, vertex.idx, end, path, limit, minimum)
            if new_path:
                if limit < minimum:
                    minimum = limit
                    shortest = new_path

    return shortest, minimum


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
    path, cost = find_path(graph, 0, len(graph) - 1, [], limit, inf)

    return path


if __name__ == '__main__':
    matrix = [[1, 5, 3],
              [4, 3, 4],
              [5, 2, 3]]
    print(if_sailor_can_take_a_trip(matrix, 3, 3, 0))