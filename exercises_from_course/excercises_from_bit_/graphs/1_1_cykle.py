"""
Napisz algorytm sprawdzający, czy graf nieskierowany posiada cykl
"""

"""
robie zmodyfikowanego dfs'a, jesli wierzcholek byl odwiedzony to znaczy ze mamy cykl
"""


def DFS_visit(graph, u, visited, parents):
    visited[u] = True
    for v in range(len(graph[u])):
        if graph[u][v] != 0:
            if not visited[v]:
                parents[v] = u
                yes_or_no = DFS_visit(graph, v, visited, parents)
                if yes_or_no is True:
                    return True
            else:
                if parents[u] != v:
                    return True


def DFS(graph):
    visited = [False for _ in range(len(graph[0]))]
    parents = [-1 for _ in range(len(graph[0]))]

    for u in range(len(graph[0])):
        if not visited[u]:
            sth = DFS_visit(graph, u, visited, parents)
            if sth is True:
                return True

    return False


graph1 = [[0, 1, 0, 0, 1],
          [1, 0, 1, 1, 0],
          [0, 1, 0, 1, 1],
          [0, 1, 1, 0, 1],
          [1, 0, 1, 1, 0]]

graph2 = [[0, 1, 0, 0],
          [1, 0, 1, 1],
          [0, 1, 0, 1],
          [0, 1, 1, 0]]
print(DFS(graph2))