"""
Znajdź długość najdłuższej ścieżki prostej w acyklicznym grafie skierowanym.
"""

"""
f(i) = najdłuzsza sceizka zaczynająca sie od wierzcholka i

f(i) = max( f(i), 1 + max( f(child1), f(child2), ...) )

"""


def DFS_visit(G, u, visited, distances):
    visited[u] = True
    for v in G[u]:
        if not visited[v]:
            DFS_visit(G, v, visited, distances)
        distances[u] = max(distances[u], 1 + distances[v])
    return distances[u]


def DFS(G):
    visited = [False for _ in range(len(G))]
    distances = [0 for _ in range(len(G))]
    for u in range(len(G)):
        if not visited[u]:
            DFS_visit(G, u, visited, distances)

    return max(distances)


G = [[1, 2],
     [3, 5],
     [1, 3],
     [4],
     [5],
     [3]]
print(DFS(G))