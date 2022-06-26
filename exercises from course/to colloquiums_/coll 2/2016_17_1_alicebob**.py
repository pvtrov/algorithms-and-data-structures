"""
Dana jest mapa kraju w postaci grafu G = (V, E), gdzie wierzchołki to miasta a krawędzie to
drogi łączące miasta. Dla każdej drogi znana jest jej długość (wyrażona w kilometrach jako liczba
naturalna). Alicja i Bob prowadzą (na zmianę) autobus z miasta x ∈ V do miasta y ∈ V ,
zamieniając się za kierownicą w każdym kolejnym mieście. Alicja wybiera trasę oraz decyduje kto
prowadzi pierwszy. Proszę zaproponować algorytm, który wskazuje taką trasę (oraz osobę, która
ma prowadzić pierwsza), żeby Alicja przejechała jak najmniej kilometrów. Algorytm powinien
być jak najszybszy (ale przede wszystkim poprawny). Proszę oszacować złożoność
zaproponowanego algorytmu, zakładając, że graf jest reprezentowany macierzowo.
"""

# cos nie działa

from cmath import inf
from queue import PriorityQueue


def print_path(parents, i, t):
    if parents[i] == -1:
        t.append(i)
        return t
    t = print_path(parents, parents[i], t)
    t.append(i)
    return t


def dijkstra(G, s, IsItAlicia):
    def relax(u, v):
        nonlocal Q
        if iteration[u]:
            dist = G[u][v]
        else:
            dist = 0

        if D[v] > D[u] + dist:
            iteration[v] = not iteration[u]
            D[v] = D[u] + dist
            Q.put((D[v], v))
            Parent[v] = u

    n = len(G)
    Q = PriorityQueue()
    D = [inf] * n
    Parent = [-1] * n
    iteration = [None] * n
    processed = [False] * n  # tablica przetworzonych wierzchołków
    if IsItAlicia:
        iteration[s] = True
    else:
        iteration[s] = False
    D[s] = 0
    Q.put((D[s], s))
    while not Q.empty():
        _, u = Q.get()
        if not processed[u]:
            for v in range(n):
                if G[u][v] > 0 and not processed[v]:
                    relax(u, v)
            processed[u] = True

    return D


def alice_and_bob(cites, s, t):
    alice = dijkstra(cites, s, True)
    bob = dijkstra(cites, s, False)
    if alice < bob:
        return "Alice", alice[t]
    else:
        return "Bob", bob[t], alice[t]


G = [[-1, -1,  6, -1, -1, -1,  5],
     [-1, -1, -1,  4, 10,  9,  8],
     [ 6, -1, -1,  5, -1, -1,  7],
     [-1,  4,  5, -1, -1, -1, -1],
     [-1, 10, -1, -1, -1,  3, -1],
     [-1,  9, -1, -1,  3, -1, -1],
     [ 5,  8,  7, -1, -1, -1, -1]]
print(alice_and_bob(G, 0, 4))
