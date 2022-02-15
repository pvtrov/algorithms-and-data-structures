from math import inf


def relax(graph, u, v, distance, parent):
    if distance[graph[u][v][0]] > distance[u] + graph[u][v][1]:
        distance[graph[u][v][0]] = distance[u] + graph[u][v][1]
        parent[graph[u][v][0]] = u


def Bellman_Ford(graph, start):
    distance = [inf for _ in range(len(graph))]
    parent = [None for _ in range(len(graph))]
    distance[start] = 0

    for u in range(len(graph)-1):
        for v in range(len(graph[u])):
            relax(graph, u, v, distance, parent)

    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if distance[graph[i][j][0]] > distance[i] + graph[i][j][1]:
                return False

    return distance, parent


if __name__ == '__main__':
    graph = [[(1, 2), (2, 4)],
             [(3, 3), (2, 3)],
             [(3, -1), (4, 2)],
             [(4, 2), (1, 3)],
             []]

    print(Bellman_Ford(graph, 0))