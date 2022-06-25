# Dany jest graf nieskierowany G zawierający n wierzchołków. Zaproponuj
# algorytm, który stwierdza czy w G istnieje cykl składający się z dokładnie 4 wierzchołków. Zakładamy, że
# graf reprezentowany jest przez macierz sasiedztwa A.


def dfs_rec(graph, vertex, path, visited):
    visited[vertex] = True
    for edge in range(len(graph[vertex])):
        if edge not in path:
            if graph[vertex][edge] == 1:
                path.append(edge)
                dfs_rec(graph, edge, path, visited)
    path.insert(0, vertex)

def DFS(graph):
    path = []
    visited = [False for _ in range(len(graph))]
    for v in range(len(graph)):
        if not visited[v]:
            dfs_rec(graph, v, path, visited)
    return path

def cycles(graph):
    path = DFS(graph)
    for i in range(len(path)-3):
        if graph[path[i]][path[i+4]] == 1:
            return "tak"
    return "nie"


if __name__ == '__main__':
    graph = [[0, 1, 1, 0, 1, 1, 0],
             [1, 0, 0, 1, 0, 1, 0],
             [1, 0, 0, 0, 1, 0, 1],
             [0, 1, 0, 0, 0, 0, 0],
             [1, 0, 1, 0, 0, 0, 0],
             [1, 1, 0, 0, 0, 0, 0],
             [0, 0, 1, 0, 0, 0, 0]]
    print(cycles(graph))