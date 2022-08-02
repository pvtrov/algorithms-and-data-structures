"""
Podaj jak najszybszy algorytm obliczający najdłuższą ścieżkę w ważonym acyklicznym grafie skierowanym.
Dany jest wierzchołek startowy
"""
from math import inf
from queue import PriorityQueue


def dijkstra_odwrotnie(graph, start):
    length_of_graph = len(graph)
    parents = [-1] * length_of_graph
    values = [-inf] * length_of_graph
    values[start] = 0
    priority_queue = PriorityQueue()
    priority_queue.put((0, start))

    while not priority_queue.empty():
        value, parent = priority_queue.get()
        for i in graph[parent]:
            if values[i[0]] < value + i[1]:
                values[i[0]] = value + i[1]
                parents[i[0]] = parent
                priority_queue.put((values[i[0]], i[0]))

    return max(values)


graph = [[[1, 5], [3, 10]],
         [[4, 3]],
         [],
         [[2, 8], [4, 7]],
         [[2, 9]]]
print(dijkstra_odwrotnie(graph, 0))