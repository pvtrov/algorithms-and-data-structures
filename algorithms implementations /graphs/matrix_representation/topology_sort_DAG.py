def dfs_rec(graph, start, path, visited):
    visited[start] = True
    for edge in range(len(graph[0])):
        if graph[start][edge] != 0:
            if edge not in path:
                dfs_rec(graph, edge, path, visited)
    path.insert(0, start)


def DFS(graph):
    path = []
    visited = [False for _ in range(len(graph[0]))]
    for u in range(len(graph[0])):
        if not visited[u]:
            dfs_rec(graph, u, path, visited)
    return path


if __name__ == '__main__':
    graph = [[0, 1, 0, 1, 1],
             [0, 0, 1, 0, 1],
             [0, 0, 0, 1, 1],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 1, 0]]

    print(DFS(graph))
