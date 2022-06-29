def DFS(u, graph, deleted, cycle, vertex_counter):
    for v in graph[u]:      # przechodze po sasiadach
        if deleted[u][v] is False:      # jesli nie krawedz jest nie usunieta to ja usuwam
            deleted[u][v] = True
            deleted[v][u] = True
            cycle = DFS(v, graph, deleted, cycle, vertex_counter)
            cycle.append(u)
            if u not in vertex_counter:
                vertex_counter.append(u)
    return cycle


def euler(graph):
    for i in range(len(graph)):
        if len(graph[i]) == 0 or len(graph[i]) % 2 != 0:
            return None

    deleted = [[False for _ in range(len(graph))] for _ in range(len(graph))]
    cycle = [0]
    vertex_counter = []
    cycle = DFS(0, graph, deleted, cycle, vertex_counter)
    if len(vertex_counter) != len(graph):
        return None
    return cycle


if __name__ == '__main__':
    graph = [[1, 2], [0, 2, 3, 5], [0, 1, 4, 5], [1, 5], [2, 5], [1, 2, 3, 4]]
    print(euler(graph))