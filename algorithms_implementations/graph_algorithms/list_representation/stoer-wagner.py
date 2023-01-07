class Node:
    def __init__(self):
        self.edges = {}

    def add_edge(self, neib, weight):
        self.edges[neib] = self.edges.get(neib, 0) + weight

    def delete_edge(self, neib):
        del self.edges[neib]


def merge_vertices(graph, v, neib):
    neighbours = list(graph[neib].edges.items())
    for vertex, weight in neighbours:
        if vertex != v:
            graph[v].add_edge(vertex, weight)
            graph[vertex].add_edge(v, weight)
        graph[neib].delete_edge(vertex)
        graph[vertex].delete_edge(neib)


def minimum_cut_phase(graph, vertices_number):
    a = 0
    S = []
    queue = PriorityQueue()
    queue.put((0, a))
    visited = [False for _ in range(vertices_number)]
    weights = [0 for _ in range(vertices_number)]
    while not queue.empty():
        weight, v = queue.get()
        if not visited[v]:
            visited[v] = True
            S.append(v)
            for neib, neib_weight in graph[v].edges.items():
                if not visited[neib]:
                    weights[neib] += neib_weight
                    queue.put((-weights[neib], neib))

    s = S[-1]
    t = S[-2]
    weight_sum = 0
    for vertex, weight in graph[s].edges.items():
        weight_sum += weight

    merge_vertices(graph, t, s)
    return weight_sum


def stoer_wagner(graph, vertices_number):
    result = inf
    number_of_undone_v = copy.copy(vertices_number)
    while number_of_undone_v > 1:
        result = min(result, minimum_cut_phase(graph, vertices_number))
        number_of_undone_v -= 1

    return result