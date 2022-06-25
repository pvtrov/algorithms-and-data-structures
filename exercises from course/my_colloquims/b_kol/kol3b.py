"""
Aga Patro, 405677
W tym zadaniu używam zmodyfikowanego algorytmu Dijkstry, z tym że musze  zmodyfikować mój graf tak by dodać jeszcze
przeloty szybcowem, tzn. muszę polączyc wszytskie wierzcholki ze sobą, gdzie wagą krawedzi bedzie suma ich opłat
z tablicy A (trzeba zapłacic za start i za lądowanie)

Złożonosć mojego algorytmu to O(n^2) (niestety funkcja make_me_good_graph daje mi złożoność n^2
<chyba, ale nie jestem do końca pewna szczerze mówiąc> )
"""

from math import inf
from queue import PriorityQueue

from kol3btesty import runtests


def make_me_good_graph(graph, fly_pays):
    for i in range(len(graph)):
        for j in range(i + 1, len(graph)):
            graph[i].append((j, fly_pays[i] + fly_pays[j]))
            graph[j].append((i, fly_pays[i] + fly_pays[j]))
    return graph


def airports(G, A, s, t):
    G = make_me_good_graph(G, A)
    n = len(G)
    distance = [inf for _ in range(n)]
    visited = [False for _ in range(n)]
    visited[s] = True
    pq = PriorityQueue()
    distance[s] = 0

    for i in range(n):
        pq.put((distance[i], i))

    while not pq.empty():
        d, v = pq.get()
        if v == t:
            return distance[t]

        for u in G[v]:
            if not visited[u[0]]:
                if distance[u[0]] > d + u[1]:
                    distance[u[0]] = d + u[1]
                    pq.put((distance[u[0]], u[0]))


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(airports, all_tests=True)
