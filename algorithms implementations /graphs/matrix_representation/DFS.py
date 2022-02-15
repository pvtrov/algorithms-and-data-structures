

def DFS_visit(graph, u, visited, parent):
    visited[u] = True
    for v in range(len(graph[u])):
        if graph[u][v] != 0:
            if not visited[v]:
                parent[v] = u
                DFS_visit(graph, v, visited, parent)


def DFS(graph):
    visited = [False for _ in range(len(graph[0]))]
    parent = [-1 for _ in range(len(graph[0]))]

    for u in range(len(graph[0])):
        if not visited[u]:
            DFS_visit(graph, u, visited, parent)

    return visited, parent


graph = [[0, 1, 0, 1, 0],
         [1, 0, 0, 1, 0],
         [0, 0, 0, 1, 1],
         [1, 1, 1, 0, 0],
         [0, 0, 1, 0, 0]]

print(DFS(graph))