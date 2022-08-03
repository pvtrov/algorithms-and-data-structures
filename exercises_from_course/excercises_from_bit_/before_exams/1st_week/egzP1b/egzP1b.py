from egzP1btesty import runtests

from math import inf
from queue import PriorityQueue


def dijkstra_from_to(G, s , airport):
    distance = [[inf for _ in range(5)] for _ in range(len(G))]
    pq = PriorityQueue()
    distance[s][0] = 0
    pq.put((0, [s, 0]))

    while not pq.empty():
        d, items = pq.get()
        vertex = items[0]
        level = items[1]

        if level != 4:
            for neib in G[vertex]:
                if distance[neib[0]][level+1] > distance[vertex][level] + neib[1]:
                    distance[neib[0]][level+1] = distance[vertex][level] + neib[1]
                    pq.put((distance[neib[0]][level+1], [neib[0], level+1]))

    return distance[airport][4]


def add_edges(new_graph, vertex1, vertex2, cost):
    new_graph[vertex1].append((vertex2, cost))
    new_graph[vertex2].append((vertex1, cost))


def make_graph(graph):
    max_ = 0
    for i in range(len(graph)):
        if graph[i][0] > graph[i][1]:
            temp_max = graph[i][0]
        else:
            temp_max = graph[i][1]
        if temp_max > max_:
            max_ = temp_max

    new_graph = [[] for _ in range(max_+1)]
    for j in range(len(graph)):
        add_edges(new_graph, graph[j][0], graph[j][1], graph[j][2])

    return new_graph


def turysta( G, D, L ):
    graph = make_graph(G)
    min_ = dijkstra_from_to(graph, D, L)
    return min_


runtests ( turysta )