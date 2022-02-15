def DFS_visit(G, u, visited, parent):
    visited[u] = True
    for v in G[u]:
        if not visited[v]:
            parent[v] = u
            DFS_visit(G, v, visited, parent)


def DFS(G):
    visited = [False for _ in range(len(G))]
    parent = [-1 for _ in range(len(G))]
    for u in range(len(G)):
        if not visited[u]:
            DFS_visit(G, u, visited, parent)
    return visited, parent


graph = [[1, 3],
         [0, 3, 4],
         [3, 4],
         [0, 1, 2],
         [1, 2]]



print(DFS(graph))
