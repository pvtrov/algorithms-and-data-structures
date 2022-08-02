"""
Zaimplementuj algorytm Floyda-Warshalla tak, aby pozostawiał informację pozwalającą na  rekonstrukcję najkrótszej
ścieżki między dwoma dowolnymi parami wierzchołków w czasie zależnym od długości tej ścieżki.
"""

from math import inf


def Floyd_Warshall(graph):
    result = []
    costs = [[inf for _ in range(len(graph))] for _ in range(len(graph))]
    parents = [[None for _ in range(len(graph))] for _ in range(len(graph))]

    for u in range(len(graph)):
        costs[u][u] = 0
        for v in range(len(graph[u])):
            parents[u][graph[u][v][0]] = v
            costs[u][graph[u][v][0]] = graph[u][v][1]

    for v in range(len(graph)):
        for u in range(len(graph)):
            for w in range(len(graph)):
                costs[u][w] = min(costs[u][w], costs[u][v] + costs[v][w])
                parents[u][w] = parents[u][v]

    for each in costs:
        result.append(each)
    return result


def getr_path(parents, u, v):
    if parents[u][v] is None:
        return []
    path = [u]
    while u != v and u is not inf and v is not inf:
        u = parents[u][v]
        path.append(u)
    return path


if __name__ == '__main__':
    graph = [[(1, 2), (2, 4)],
             [(2, 3), (3, 3)],
             [(3, -1), (4, -2)],
             [(4, 4), (3, 3)],
             []]
    res = Floyd_Warshall(graph)
    print(getr_path(res, 0, 2))