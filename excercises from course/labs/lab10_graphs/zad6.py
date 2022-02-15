# Dany jest acykliczny, spójny nieskierowany, ważony graf T (czyli T jest
# tak naprawdę ważonym drzewem). Proszę wskazać algorytm, który znajduje taki wierzchołek T, z którego
# odległość do najdalszego wierzchołka jest minimalna.\

"""
1. dla kazdego wierzcholka szukam najdluzszej sciezki ( nie patrzac na wagi )
2. licze sume wagi i zwracam ten wierzcholek któy ma najmniejsza sume wag w swojej najdluzszej sciezce
"""
from math import inf
from queue import Queue


def BFS(graph, start):
    queue = Queue()
    visited = [False for _ in range(len(graph))]
    distance = [-1 for _ in range(len(graph))]
    parent = [None for _ in range(len(graph))]

    distance[start] = 0
    visited[start] = True
    queue.put(start)

    while queue.qsize():
        u = queue.get()
        for v in graph[u]:
            if not visited[v[0]]:
                visited[v[0]] = True
                distance[v[0]] = distance[u] + 1
                parent[v[0]] = u
                queue.put(v[0])

    return distance, parent


def create_path(parent, vertex, path):
    if parent[vertex] is not None:
        path.append(vertex)
        create_path(parent, parent[vertex], path)
    path.reverse()
    return path


def suming(graph, path):
    sum = 0
    for i in range(len(path)-1):
        for j in range(len(graph[path[i]])):
            if graph[path[i]][j][0] == path[i+1]:
                sum += graph[path[i]][j][1]
    return sum


def best_root(graph):
    really_min_sum = inf
    result = 0
    for i in range(len(graph)):
        distance, parent = BFS(graph, i)
        max_distance = max(distance)
        min_sum = inf
        for j in range(len(distance)):
            path = []
            if distance[j] == max_distance:
                path = create_path(parent, j, path)
                path.insert(0, i)
                temp_sum = suming(graph, path)
                min_sum = min(min_sum, temp_sum)

        if min_sum < really_min_sum:
            really_min_sum = min_sum
            result = i
    return result



graph = [[[2, 8]],
         [[2, 5]],
         [[0, 8], [1, 5], [3, 6]],
         [[2, 6], [4, 7], [5, 9]],
         [[3, 7]],
         [[3, 9], [6, 4], [7, 6]],
         [[5, 4]],
         [[5, 6]]]

print(best_root(graph))