

def searching(graph, source, sink, parent):
    visited = [False for _ in range(len(graph))]
    queue = []

    queue.append(source)
    visited[source] = True

    while queue:
        u = queue.pop(0)
        for index, value in enumerate(graph[u]):
            if visited[index] == False and value > 0:
                queue.append(index)
                visited[index] = True
                parent[index] = u

    return True if visited[sink] else False


def ford_fulkerson(graph, source, sink):
    parent = [-1 for _ in range(len(graph))]
    max_flow = 0

    while searching(graph, source, sink, parent):
        path_flow = float("inf")
        output = sink
        while output != source:
            path_flow = min(path_flow, graph[parent[output]][output])
            output = parent[output]

        max_flow += path_flow
        v = sink

        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]

    return max_flow


if __name__ == '__main__':
    graph = [[0, 30, 25, 0, 0, 0],
             [0, 0, 24, 0, 0, 0],
             [0, 0, 0, 26, 23, 18],
             [0, 0, 0, 0, 0, 30],
             [0, 0, 0, 0, 0, 21],
             [0, 0, 0, 0, 0, 0]]
    print(ford_fulkerson(graph, 0, 5))

