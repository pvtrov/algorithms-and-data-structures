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


G = [[1, 2], [0, 2, 4], [0, 1], [4, 5], [1, 3, 5], [3, 4]]
# G = [[1, 2], [0, 2], [0, 1, 3], [2]]
print(bridge(G))