"""
Dany jest ciąg przedziałów postaci [ai, bi]. Dwa przedziały można skleić, jeśli mają dokładnie jeden punkt wspólny.
Podaj algorytm, który sprawdza, czy da się uzyskać przedział [a, b] poprzez sklejanie odcinków.
"""


def make_graph(ranges):
    graph = [[] for _ in range(len(ranges))]

    for i in range(len(ranges)):
        a = ranges[i][0]
        b = ranges[i][1]
        for j in range(i, len(ranges)):
            if a == ranges[j][1] or b == ranges[j][0]:
                graph[i].append(j)
                graph[j].append(i)

    return graph


def find_glue(ranges, graph, start_vertex, ends, path):
    path = path + [start_vertex]
    if start_vertex in ends:
        return path

    if len(graph[start_vertex]) == 0:
        return None

    for neighbour in graph[start_vertex]:
        if neighbour not in path:
            return find_glue(ranges, graph, neighbour, ends, path)


def gluing_ranges(ranges, a, b):
    start_vertexs = []
    end_vertexs = []
    graph = make_graph(ranges)

    for i in range(len(ranges)):
        if a == ranges[i][0]:
            start_vertexs.append(i)
        elif b == ranges[i][1]:
            end_vertexs.append(i)

    for i in range(len(start_vertexs)):
        if find_glue(ranges, graph, start_vertexs[i], end_vertexs, []) is not None:
            return True

    return False


ranges = [[0, 1], [2, 5], [3, 4], [5, 8], [2, 3], [1, 2], [4, 5], [2, 7]]
print(gluing_ranges(ranges, 0, 7))