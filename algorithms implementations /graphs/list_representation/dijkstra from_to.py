from math import inf
from queue import PriorityQueue


def dijkstra_from_to(G, s , t):
    n = len(G)
    distance = [inf for _ in range(n)]
    parent = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]
    visited[s] = True
    pq = PriorityQueue()
    distance[s] = 0

    for i in range(n):
        pq.put((distance[i], i))
    while not pq.empty():
        d, v = pq.get()
        if v == t:
            # printsolution(distance, parent, s)
            return parent, distance[t]

        for u in G[v]:
            if visited[u[0]] is False:
                if distance[u[0]] > d + u[1]:
                    distance[u[0]] = d + u[1]
                    parent[u[0]] = v
                    pq.put((distance[u[0]], u[0]))


graph = [[(1, 2), (2, 4)],
         [(0, 2), (3, 11), (4, 3)],
         [(0, 4), (3, 13)],
         [(1, 11), (2, 13), (5, 17), (6, 1)],
         [(1, 3), (5, 5)],
         [(3, 17), (4, 5), (7, 7)],
         [(3, 1), (7, 3)],
         [(5, 7), (6, 3), ]]

print(dijkstra_from_to(graph, 0, 7))
