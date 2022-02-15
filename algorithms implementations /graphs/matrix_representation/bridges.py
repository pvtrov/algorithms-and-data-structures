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


if __name__ == '__main__':
    # graph = [[0, 1, 1, 0],
    #          [1, 0, 1, 0],
    #          [1, 1, 0, 1],
    #          [0, 0, 1, 0]]
    graph = [[0, 1, 1, 0, 0, 0],
             [1, 0, 1, 0, 1, 0],
             [1, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 1],
             [0, 1, 0, 1, 0, 1],
             [0, 0, 0, 1, 1, 0]]

    print(bridge(graph))