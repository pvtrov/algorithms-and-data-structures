def bfs(graph, flow, source, sink):
    queue = [source]
    paths = {source: []}
    if source == sink:
        return paths[source]
    while queue:
        u = queue.pop(0)
        for vertex in range(len(graph[u])):
            if (graph[u][vertex] - flow[u][vertex] > 0) and vertex not in paths:
                paths[vertex] = paths[u] + [(u, vertex)]
                if vertex == sink:
                    return paths[vertex]
                queue.append(vertex)
    return None


def edmond_karp(graph, source, sink):
    length = len(graph)
    flows = [[0 for _ in range(length)] for _ in range(length)]
    path = bfs(graph, flows, source, sink)

    while path is not None:
        flow = min(graph[u][v] - flows[u][v] for u, v in path)
        for u, v in path:
            flows[u][v] += flow
            flows[v][u] -= flow
        path = bfs(graph, flows, source, sink)
    return sum(flows[source][i] for i in range(length))


if __name__ == '__main__':
    graph = [[0, 8, 0, 0, 3, 0],
             [0, 0, 9, 0, 0, 0],
             [0, 0, 0, 0, 7, 2],
             [0, 0, 0, 0, 0, 5],
             [0, 0, 0, 4, 0, 0],
             [0, 0, 0, 0, 0, 0]]
    # graph = [[0, 30, 25, 0, 0, 0],
    #          [0, 0, 24, 0, 0, 0],
    #          [0, 0, 0, 26, 23, 18],
    #          [0, 0, 0, 0, 0, 30],
    #          [0, 0, 0, 0, 0, 21],
    #          [0, 0, 0, 0, 0, 0]]
    print(edmond_karp(graph, 0, 5))
