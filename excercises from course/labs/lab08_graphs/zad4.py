# Dany jest graf G = (V, E), gdzie każda krawędź ma wagę ze zbioru
# {1, . . . , ∣E∣} (wagi krawędzi są parami różne). Proszę zaproponować algorytm, który dla danych wierzchołków
# x i y sprawdza, czy istnieje ścieżka z x do y, w której przechodzimy po krawędziach o coraz mniejszych wagach.

from math import inf


def decreasing_path(graph, start, end, path, weight):
    path = path + [start]

    if start == end:
        return path

    if len(graph[start]) == 0:
        return None

    for node in graph[start]:
        if node[0] not in path and node[1] < weight:
            weight = node[1]
            new_path = decreasing_path(graph, node[0], end, path, weight)
            if new_path:
                return new_path
    return None


if __name__ == '__main__':
    graph = [[(1, 1), (6, 2)],
             [(0, 1), (2, 4), (5, 3)],
             [(3, 5), (1, 4)],
             [(2, 5), (4, 8), (5, 7), (6, 9)],
             [(5, 10), (3, 8)],
             [(4, 10), (3, 7), (1, 3), (6, 8)],
             [(5, 8), (3, 9), (0, 2)]]
    path = []
    print(decreasing_path(graph, 3, 0, path, inf))
