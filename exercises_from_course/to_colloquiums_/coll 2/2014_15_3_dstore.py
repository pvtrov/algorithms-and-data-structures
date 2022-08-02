"""
W miasteczku są sklepy i domy. Trzeba sprawdzić jak daleko do najbliższego sklepu mają mieszkańcy.

struct Vertex {
bool shop; // true-sklep, false-dom
int* distances; // tablica odległości do innych wierzchołków
int* edges; // numery wierzchołków opisanych w distances
int edge; // rozmiar tablicy distances (i edges)
int d store; // odległość do najbliższego sklepu
};

Zaimplementować funkcję distanceToClosestStore (int n, Vertex* village)
uzupełniającą d store dla tablicy Vertexów i oszacować złożoność algorytmu.
"""
"""
O(liczba miast * dijkstra)
"""

from queue import PriorityQueue
from math import inf


def dijkstra(graph, start, shops):
    length_of_graph = len(graph)
    parents = [-1] * length_of_graph
    values = [inf] * length_of_graph
    values[start] = 0
    priority_queue = PriorityQueue()
    priority_queue.put((0, start))

    while not priority_queue.empty():
        value, parent = priority_queue.get()
        for i in graph[parent]:
            if values[i[0]] > value + i[1]:
                values[i[0]] = value + i[1]
                parents[i[0]] = parent
                priority_queue.put((values[i[0]], i[0]))

    distances = []
    for i in range(len(values)):
        if shops[i]:
            distances.append(values[i])

    return min(distances)


def d_store(graph, shops):
    d = []

    for i in range(len(graph)):
        if not shops[i]:
            d.append((i, dijkstra(graph, i, shops)))

    return d


graph = [[(1, 5), (3, 2), (4, 3)],
         [(0, 5), (2, 3), (5, 5)],
         [(1, 3), (5, 6)],
         [(0, 2)],
         [(0, 3), (5, 4)],
         [(1, 5), (2, 6), (4, 4)]]
is_this_shop = [False, True, False, False, True, False]
print(d_store(graph, is_this_shop))