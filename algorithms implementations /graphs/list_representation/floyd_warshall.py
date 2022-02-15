from math import inf


def Floyd_Warshall(graph):
    result = []
    costs = [[inf for _ in range(len(graph))] for _ in range(len(graph))]

    for u in range(len(graph)):
        costs[u][u] = 0
        for v in range(len(graph[u])):
            costs[u][graph[u][v][0]] = graph[u][v][1]

    for v in range(len(graph)):
        for u in range(len(graph)):
            for w in range(len(graph)):
                costs[u][w] = min(costs[u][w], costs[u][v] + costs[v][w])

    for each in costs:
        result.append(each)
    return result


if __name__ == '__main__':
    graph = [[(1, 2), (2, 4)],
             [(2, 3), (3, 3)],
             [(3, -1), (4, -2)],
             [(4, 4), (3, 3)],
             []]
    print(Floyd_Warshall(graph))