from zad3testy import runtests
from math import inf
from queue import PriorityQueue

"""
Dana jest tablica T zawierająca N liczb naturalnych. Z pozycji a można przeskoczyć na pozycję b
jeżeli liczby T[a] i T[b] mają co najmniej jedną wspólną cyfrę. Koszt takego skoku równy ∣T[a] −
T[b]∣. Proszę napisać funkcję, która wyznacza minimalny sumaryczny koszt przejścia z najmniejszej
do największej liczby w tablicy T. Jeżeli takie przejście jest niemożliwe, funkcja powinna zwrócić
wartość -1.
"""
"""
z danej tablicy tworzymy graf i odpalamy dijkstre
"""


def divide(P):
    new_P = [[] for _ in range(len(P))]

    for i in range(len(P)):
        while P[i] > 0:
            c = P[i] % 10
            new_P[i].append(c)
            P[i] = P[i] // 10

    return new_P


def dijkstra_from_to(G, s, t):
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
            return distance[t]

        for u in G[v]:
            if visited[u[0]] is False:
                if distance[u[0]] > d + u[1]:
                    distance[u[0]] = d + u[1]
                    parent[u[0]] = v
                    pq.put((distance[u[0]], u[0]))


def make_graph(P, old_P):
    graph = [[] for _ in range(len(P))]

    for i in range(len(P)):
        for j in range(len(P)):
            if i != j:
                c = [s for s in P[i] if s in P[j]]
                if len(c) > 0:  # da sie skoczyc
                    weight = abs(old_P[i] - old_P[j])
                    graph[i].append((j, weight))
                    graph[j].append((i, weight))

    return graph


def find_cost(P):
    old_P = P.copy()
    max_val = -inf
    min_val = inf
    for i in range(len(P)):
        if max_val < P[i]:
            max_index = i
            max_val = P[i]

        if min_val > P[i]:
            min_index = i
            min_val = P[i]

    new_P = divide(P)

    graph = make_graph(new_P, old_P)
    min_cost = dijkstra_from_to(graph, min_index, max_index)
    if min_cost == inf:
        return -1

    return min_cost


runtests(find_cost)
