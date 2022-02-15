from math import inf


def BFS(graph, flow, source, sink):
    queue = [source]
    paths = {source: []}
    if source == sink:
        return paths[source]

    while queue:
        u = queue.pop(0)
        for vertex in range(len(graph[u])):
            if (graph[u][vertex][1] - flow[u][graph[u][vertex][0]] > 0) and graph[u][vertex][0] not in paths:
                paths[graph[u][vertex][0]] = paths[u] + [(u, graph[u][vertex][0])]
                if graph[u][vertex][0] == sink:
                    return paths[graph[u][vertex][0]]
                queue.append(graph[u][vertex][0])
    return None


def Edmond_Karp(graph, source, sink):
    length = len(graph)
    flows = [[0 for _ in range(length)] for _ in range(length)]
    path = BFS(graph, flows, source, sink)

    while path is not None:
        min_flow = inf
        for u, v in path:
            for i in range(len(graph[u])):
                if v == graph[u][i][0]:
                    flow = graph[u][i][1] - flows[u][v]
                    if min_flow > flow:
                        min_flow = flow
        for u, v in path:
            flows[u][v] += min_flow
            flows[v][u] -= min_flow
        path = BFS(graph, flows, source, sink)

    return sum(flows[source][i] for i in range(length))


if __name__ == '__main__':
    graph = [[(1, 8), (4, 3)],
             [(2, 9)],
             [(4, 7), (5, 2)],
             [(5, 5)],
             [(3, 4)],
             []]
    # graph =[[[1, 30], [2, 25]],
    #         [[2, 24]],
    #         [[3, 26], [4, 24], [5, 18]],
    #         [[5, 30]],
    #         [[5, 21]],
    #         []]
    print(Edmond_Karp(graph, 0, 5))