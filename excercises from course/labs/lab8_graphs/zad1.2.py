# 2. Policzyć liczbę spójnych składowych w grafie (implementacja przeciwna do tej z poprzedniego zadania)

def DFS_visit(G, u, visited):
    visited[u] = True
    for v in G[u]:
        if not visited[v]:
            DFS_visit(G, v, visited)
    return visited


def component(graph):
    counter = 0
    visited = [False for _ in range(len(graph))]
    for vertex in range(len(graph)):
        if not visited[vertex]:
            visited = DFS_visit(graph, vertex, visited)
            counter += 1
    return counter


if __name__ == '__main__':
    graph = [[1, 9],
             [0, 2],
             [1, 9],
             [4, 5],
             [3, 5],
             [3, 4],
             [7, 10],
             [8, 6],
             [7, 10],
             [0, 2],
             [6, 8]]
    print(component(graph))
