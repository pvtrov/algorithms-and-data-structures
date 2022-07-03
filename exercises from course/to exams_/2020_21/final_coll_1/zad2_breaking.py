from queue import PriorityQueue

from zad2testy import runtests

"""
znajdujemy mosty i liczymy ktory wierzcholek powtarza sie najczedciej
"""


class vertex:
    def __init__(self):
        self.visited = False
        self.d = -1
        self.low = -1
        self.parent = -1


def DFSb(graph, v, number, vertices, result):
    vertices[v].visited = True
    number += 1
    vertices[v].d = vertices[v].low = number
    for w in range(len(graph)):
        if graph[v][w] != 0:
            if not vertices[w].visited:
                vertices[w].parent = v
                number, vertices, result = DFSb(graph, w, number, vertices, result)
                vertices[v].low = min(vertices[v].low, vertices[w].low)
                if vertices[w].low == vertices[w].d:
                    result.append((w, vertices[w].parent))
            elif w != vertices[v].parent:
                vertices[v].low = min(vertices[v].low, vertices[w].d)

    return number, vertices, result


def bridge(graph):
    length = len(graph)
    vertices = [vertex() for _ in range(length)]
    number = 0
    result = []
    for u in range(length):
        if not vertices[u].visited:
            number, vertices, result = DFSb(graph, u, number, vertices, result)

    return result


def count_edges(graph, vertexs):
    edges_number = PriorityQueue()

    for vertex in vertexs:
        counter = 0
        for j in range(len(graph)):
            if graph[vertex][j] == 1:
                counter += 1
        edges_number.put((-counter, vertex))

    _, result = edges_number.get()
    return result


def give_me_right_vertex(graph, bridges):
    ver_number = [0] * len(graph)

    for edge in bridges:
        ver_number[edge[0]] += 1
        ver_number[edge[1]] += 1

    max_vert = []
    max_ = max(ver_number)

    for i in range(len(ver_number)):
        if ver_number[i] == max_:
            max_vert.append(i)

    if len(max_vert) == 1:
        return max_vert[0]
    else:
        return count_edges(graph, max_vert)


def breaking(G):
    bridges = bridge(G)
    print(bridges)
    if not bridges:
        return None

    vertex = give_me_right_vertex(G, bridges)
    return vertex


runtests( breaking )