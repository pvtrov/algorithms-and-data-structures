from egzP5btesty import runtests

# O(nlogn)

class vert:
    def __init__(self):
        self.visited = False
        self.d = -1
        self.low = -1
        self.parent = -1


def DFSb(G, v, nr,vertices, result):
    vertices[v].visited = True
    nr += 1
    vertices[v].d = vertices[v].low = nr
    for w in G[v]:
        if not vertices[w].visited:
            vertices[w].parent = v
            nr, vertices, result = DFSb(G, w, nr,vertices, result)
            vertices[v].low = min(vertices[v].low, vertices[w].low)
            if vertices[w].low == vertices[w].d:
                result.append((w, vertices[w].parent))
        elif w != vertices[v].parent:
            vertices[v].low = min(vertices[v].low, vertices[w].d)
    return nr, vertices, result


def bridge(G):
    n = len(G)
    vertices = [vert() for _ in range(n)]
    nr = 0
    result = []
    for u in range(len(G)):
        if not vertices[u].visited:
            nr, vertices, result = DFSb(G,u,nr, vertices, result)

    return result


def make_list_graph(graph, B):
    for i in B:
        if i[1] not in graph[i[0]]:
            graph[i[0]].append(i[1])
        if i[0] not in graph[i[1]]:
            graph[i[1]].append(i[0])
    return graph


def koleje ( B ):
    max_ = -1
    for i in range(len(B)):
        if max_ < B[i][0]:
            max_ = B[i][0]
        if max_ < B[i][1]:
            max_ = B[i][1]
    graph = [[] for _ in range(max_+1)]
    make_list_graph(graph, B)
    bridges = bridge(graph)
    stations = [0] * (max_+1)

    for i in bridges:
        if len(graph[i[0]]) > 1:
            stations[i[0]] += 1
        if len(graph[i[1]]) > 1:
            stations[i[1]] += 1

    sum_ = 0
    for i in range(len(stations)):
        if stations[i] > 0:
            sum_ += 1

    return sum_


runtests ( koleje, all_tests=True )
# B = [
#     (3, 1), (0, 1), (4, 2),
#     (1, 2), (0, 1), (2, 4),
#     (2, 4), (0, 3), (2, 4),
#     (1, 0), (2, 1)
# ]
# print(koleje(B))