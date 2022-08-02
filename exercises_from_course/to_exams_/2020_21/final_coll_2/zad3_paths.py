from math import inf
from queue import PriorityQueue

from zad3testy import runtests
"""
Dany jest nieskierowany graf G = (V, E) oraz dwa wierzchołki, s i t. Proszę zaimplementować
funkcję:
def paths( G,s,t ):
...
która zwraca liczbę krawędzi e takich, że e występuje na pewnej najkrótszej ścieżce z s do t. Graf
dany jest jako lista list sąsiedztwa w postaci [(v 0 , w 0 ), (v 1 , w 1 ), ...], gdzie: v i to numer wierzchołka,
w i to waga krawędzi prowadzącej do wierzchołka v i . Wagi krawędzi są dodatnie.
Funkcja powinna być możliwie jak najszybsza. Proszę oszacować złożoność czasową i pamięciową
użytego algorytmu.

Przykład.
Dla listy sąsiedztwa postaci:
G = [ [(1,2),(2,4)],
[(0,2),(3,11),(4,3)],
[(0,4),(3,13)],
[(1,11),(2,13),(5,17),(6,1)],
[(1,3),(5,5)],
[(3,17),(4,5),(7,7)],
[(3,1),(7,3)],
[(5,7),(6,3)] ],
s = 0, t = 7
# sąsiedzi i wagi wierzchołka nr 0
# sąsiedzi i wagi wierzchołka nr 1
# itd.
funkcja powinna zwrócić wartość 7. Krawędzie 0-1, 1-4, 4-5, 5-7, 1-3, 3-6, 6-7.
"""


def printpath(parent, i, t):
    if parent[i] == -1:
        t.append(i)
        return t
    t = printpath(parent, parent[i], t)
    t.append(i)
    return t


def dijkstra_from_to(G, s, t):
    n = len(G)
    distance = [inf for _ in range(n)]
    pre = [[] for _ in range(n)]
    visited = [False for _ in range(n)]
    visited[s] = True
    pq = PriorityQueue()
    distance[s] = 0

    for i in range(n):
        pq.put((distance[i], i))
    while not pq.empty():
        d, v = pq.get()
        if v == t:
            return pre, distance[t], distance

        for u in G[v]:
            if distance[u[0]] == d + u[1]:
                pre[u[0]].append(v)
            elif distance[u[0]] > d + u[1]:
                distance[u[0]] = d + u[1]
                pre[u[0]] = [v]
                pq.put((distance[u[0]], u[0]))


def make_paths(prevs, vertex, paths):
    for neib in prevs[vertex]:
        paths.add((vertex, neib))
        make_paths(prevs, neib, paths)


def paths(G, s, t):
    parent, min_distance, distances = dijkstra_from_to(G, s, t)
    path = set()
    make_paths(parent, t, path)

    return len(path)


runtests(paths)
# G =  [[(1,2),(2,4)],
#       [(0,2),(3,11),(4,3)],
#       [(0,4),(3,13)],
#       [(1,11),(2,13),(5,17),(6,1)],
#       [(1,3),(5,5)],
#       [(3,17),(4,5),(7,7)],
#       [(3,1),(7,3)],
#       [(5,7),(6,3)] ]
#
# s = 0
# t = 7
# print(paths(G, s, t))

