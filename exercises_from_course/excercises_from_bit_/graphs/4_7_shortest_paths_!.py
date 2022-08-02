"""
Oprócz długości krawędzi, graf ma przypisane koszty wierzchołków.
Zdefiniujmy koszt ścieżki jako sumę kosztów jej krawędzi oraz sumę kosztów wierzchołków (wraz z końcami).

Jak znaleźć najtańsze ścieżki między wierzchołkiem startowym a wszystkimi pozostałymi?

Podaj rozwiązanie zarówno dla grafu skierowanego, jak i nieskierowanego.
"""
from queue import PriorityQueue
from math import inf


def dijkstra(graph, start):
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

    return values, parents

