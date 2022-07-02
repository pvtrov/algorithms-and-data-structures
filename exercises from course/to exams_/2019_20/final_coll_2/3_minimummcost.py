"""
Dana jest tablica T zawierająca N liczb naturalnych. Z pozycji a można przeskoczyć na pozycję b
jeżeli liczby T[a] i T[b] mają co najmniej jedną wspólną cyfrę. Koszt takego skoku równy ∣T[a] −
T[b]∣. Proszę napisać funkcję, która wyznacza minimalny sumaryczny koszt przejścia z najmniejszej
do największej liczby w tablicy T. Jeżeli takie przejście jest niemożliwe, funkcja powinna zwrócić
wartość -1.
"""
from math import inf
from queue import PriorityQueue


def are_connected(f_word, s_word):
    f_table = [0] * 10

    for letter in f_word:
        f_table[int(letter)] += 1

    for letter in s_word:
        if f_table[int(letter)] > 0:
            return True

    return False


def make_graph(table):
    table.sort()
    graph = [[0] * len(table) for _ in range(len(table))]

    for i in range(len(table)):
        for j in range(i + 1, len(table)):
            if are_connected(str(table[i]), str(table[j])):
                wage = abs(table[i] - table[j])
                graph[i][j] = wage
                graph[j][i] = wage

    return graph


def dijkstra1(G, s, t):  # między podanymi wierzchołkami
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
        for u in range(n):
            if G[v][u] != 0 and visited[u] == False:
                if distance[v] + G[v][u] < distance[u]:
                    distance[u] = distance[v] + G[v][u]
                    parent[u] = v
                    pq.put((distance[u], u))


def minimum_cost(table):
    graph = make_graph(table)
    res = dijkstra1(graph, 0, len(graph) - 1)
    if res == inf:
        return -1

    return res


T =  [587,990,257,246,668,132]
print(minimum_cost(T))
