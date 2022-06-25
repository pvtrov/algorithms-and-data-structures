"""
W miasteczku są sklepy i domy. Trzeba sprawdzić jak daleko do najbliższego sklepu mają mieszkańcy.
struct Vertex {
bool shop; // true-sklep, false-dom
int* distances; // tablica odległości do innych wierzchołków
int* edges; // numery wierzchołków opisanych w distances
int edge; // rozmiar tablicy distances (i edges)
int d_store; // odległość do najbliższego sklepu
};
Zaimplementować funkcję
distanceToClosestStore (int n, Vertex* village) uzupełniającą d_store dla tablicy Vertexów i oszacować złożoność algorytmu.
"""

from queue import Queue
from math import inf


def BFS(graph, start, is_this_shop):
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
            if not visited[v]:
                visited[v] = True
                distance[v] = distance[u] + 1
                parent[v] = u
                queue.put(v)

    minimum = inf
    for i in range(len(distance)):
        if is_this_shop[i] and minimum > distance[i]:
            minimum = distance[i]

    return minimum


def find_closest_shop(graph, is_this_shop):
    closest_shop = []
    for i in range(len(is_this_shop)):
        if not is_this_shop[i]:
            closest_shop.append((i, BFS(graph, i, is_this_shop)))

    return closest_shop


graph = [[1, 3, 4],
         [0, 2, 5],
         [1, 5],
         [0],
         [0, 5],
         [1, 2, 4]]
is_this_shop = [False, True, False, False, True, False]
print(find_closest_shop(graph, is_this_shop))