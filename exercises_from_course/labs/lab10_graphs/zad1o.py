# Dany jest graf G = (V, E), gdzie każda krawędź ma wagę
# ze zbioru {1, . . . , ∣E∣} (wagi krawędzi są parami różne). Proszę zaproponować algorytm, który dla danych
# wierzchołków x i y oblicza ścieżkę o najmniejszej sumie wag, która prowadzi z x do y po krawędziach o
# malejących wagach (jeśli ścieżki nie ma to zwracamy ∞).

# odpalam dijkstre ale tylko dla malejąćych (relaklsuje te o mniejszej wadze
# cos nie dziala w kodzie
from math import inf
from queue import PriorityQueue


def printpath(parent, i, t):
    if parent[i] == -1:
        t.append(i)
        return t
    t = printpath(parent, parent[i], t)
    t.append(i)
    return t


def printsolution(distance, parent, s):
    for i in range(1, len(distance)):
        print(printpath(parent, i, []))


def decreasing_dijkstra(graph, start, end):
    length = len(graph)
    distance = [inf for _ in range(length)]
    parent = [-1 for _ in range(length)]
    visited = [False for _ in range(length)]
    visited[start] = True
    queue = PriorityQueue()
    distance[start] = 1
    min_distance = inf

    for i in range(length):
        queue.put((distance[i], i))
    while not queue.empty():
        d, vertex = queue.get()
        if vertex == end:
            printsolution(distance, parent, start)
            return parent
        for u in range(length):
            if graph[vertex][u] != 0 and visited[u] == False and graph[vertex][u] < min_distance:
                if distance[vertex] * graph[vertex][u] < distance[u]:
                    distance[u] = distance[vertex] * graph[vertex][u]
                    parent[u] = vertex
                    queue.put((distance[u], u))
                    min_distance = graph[vertex][u]
                else:
                    continue

    printsolution(distance, parent, start)


if __name__ == '__main__':
    graph = [[0, 9, 0, 0, 5, 6],
             [9, 0, 8, 2, 4, 0],
             [0, 8, 0, 1, 0, 7],
             [0, 2, 1, 0, 0, 0],
             [5, 4, 0, 0, 0, 0],
             [6, 0, 7, 0, 0, 0]]

    print(decreasing_dijkstra(graph, 0, 2))
