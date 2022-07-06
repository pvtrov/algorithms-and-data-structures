def dfs_rec(graph, start, path, visited):
    visited[start] = True
    for edge in graph[start]:
        if edge not in path and not visited[edge]:
            # print(edge, path)
            dfs_rec(graph, edge, path, visited)
    path.insert(0, start)


def DFS(G):
    path = []
    visited = [False for _ in range(len(G))]
    for u in range(len(G)):
        if not visited[u]:
            dfs_rec(G, u, path, visited)
    return path


if __name__ == '__main__':

    G = [[1, 3, 4], [4, 2], [3, 4], [], [3]]
    print(DFS(G))