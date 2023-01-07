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


graph = [ [(1,2),(2,4)],
      [(0,2),(3,11),(4,3)],
      [(0,4),(3,13)],
      [(1,11),(2,13),(5,17),(6,1)],
      [(1,3),(5,5)],
      [(3,17),(4,5),(7,7)],
      [(3,1),(7,3)],
      [(5,7),(6,3),] ]

print(dijkstra(graph, 0))
