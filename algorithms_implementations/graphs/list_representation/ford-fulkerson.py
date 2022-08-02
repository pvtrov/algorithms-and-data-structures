from math import inf


def searching(graph, source, sink, parent):
    visited = [False for _ in range(len(graph))]
    queue = []

    queue.append(source)
    visited[source] = True

    while queue:
        u = queue.pop(0)
        for j in range(len(graph[u])):
            index, value = graph[u][j]
            if visited[index] is False and value > 0:
                queue.append(index)
                visited[index] = True
                parent[index] = u

    if visited[sink]:
        return True
    else:
        return False


def ford_fulkerson(graph, source, sink):
    global path_flow
    parent = [-1 for _ in range(len(graph))]
    max_flow = 0

    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j][1] != 0:
                graph[graph[i][j][0]].append([i, 0])

    while searching(graph, source, sink, parent):
        path_flow = inf
        output = sink

        while output != source:
            if graph[parent[output]][output] < path_flow:
                path_flow = graph[parent[output]][output]
            output = parent[output]

        max_flow += path_flow
        v = sink

        while v != source:  # tutaj pogrzebac i powinoo byc w pyte
            u = parent[v]
            for i in range(len(graph[u])):
                if v == graph[u][i][0]:
                    graph[u][i][1] -= path_flow
            for j in range(len(graph[v])):
                if u == graph[v][j][0]:
                    graph[v][j][1] += path_flow

            v = parent[v]

    return max_flow


if __name__ == '__main__':
    graph = [[[3, 1], [4, 1], [5, 1]],
             [[3, 1], [4, 1], [5, 1]],
             [[3, 1], [4, 1], [5, 1]],
             [[0, 1], [1, 1], [2, 1]],
             [[0, 1], [1, 1], [2, 1]],
             [[0, 1], [1, 1], [2, 1]]
             ]
    print(ford_fulkerson(graph, 0, 5))
