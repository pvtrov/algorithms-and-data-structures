# Przewodnik chce przewieźć grupę K turystów z
# miasta A do miasta B. Po drodze jest jednak wiele innych miast i między różnymi miastami jeżdzą autobusy o
# różnej pojemności. Mamy daną listę trójek postaci (x, y, c), gdzie x i y to miasta między którymi bezpośrednio
# jeździ autobus o pojemności c pasażerów.
# Przewodnik musi wyznaczyć wspólną trasę dla wszystkich tursytów i musi ich podzielić na grupki tak,
# żeby każda grupka mogła przebyć trasę bez rodzielania się. Proszę podać algorytm, który oblicza na ile
# (najmniej) grupek przewodnik musi podzielić turystów (i jaką trasą powinni się poruszać), źeby wszyscy
# dostali się z A do B.

# wybieram trase która ma najwiekszy flow i dziele ilosc turystow przez ten flow

from math import inf
from queue import Queue
from math import ceil

def BFS(G, s, t, parent):
    Q = Queue()
    visited = [False] * len(G)
    distance = [-1] * len(G)

    visited[s] = True
    distance[s] = 0

    Q.put(s)

    while Q.qsize() != 0:
        u = Q.get()
        for each in range(len(G)):
            if G[u][each] != 0 and not visited[each]:
                visited[each] = True
                distance[each] = distance[u] + 1
                parent[each] = u
                Q.put(each)

    return visited[t]


def Ford_Fulkerson(G, s, t):
    n = len(G)
    parents = [None] * n
    flow = 0
    while BFS(G, s, t, parents):
        current = t
        cur_flow = float("inf")

        while (current != s):
            if G[parents[current]][current] < cur_flow:
                cur_flow = G[parents[current]][current]
            current = parents[current]
        flow += cur_flow
        v = t
        while (v != s):
            G[parents[v]][v] -= cur_flow
            G[v][parents[v]] += cur_flow
            v = parents[v]
    return flow


def MaxFlowUndirected(G):
    n = len(G)
    E = 0
    for u in range(len(G)):
        for v in range(u, len(G)):
            if G[u][v] != 0:
                E += 1
    directedG = [[0 for _ in range(n + E)] for _ in range(n + E)]

    curr = n
    for u in range(n):
        for v in range(u, n):
            if G[u][v] != 0:
                directedG[u][v] = G[u][v]
                directedG[v][curr] = G[u][v]
                directedG[curr][u] = G[u][v]
                curr += 1
    return Ford_Fulkerson(directedG, 0, 4)


def list_to_graph(list):
    maximum = -inf
    for i in range(len(list)):
        j = 0
        while j <= 1:
            if list[i][j] > maximum:
                maximum = list[i][j]
                j += 1
            else:
                j += 1

    maximum += 1

    graph = [[0 for _ in range(maximum)] for _ in range(maximum)]
    for i in range(len(list)):
        graph[list[i][0]][list[i][1]] = list[i][2]
        graph[list[i][1]][list[i][0]] = list[i][2]

    return graph


def tourists(list, K):
    graph = list_to_graph(list)
    max_flow = MaxFlowUndirected(graph)
    number_of_groups = ceil(K/max_flow)
    return number_of_groups


if __name__ == '__main__':
    list = [[0, 3, 5], [0, 4, 10], [1, 3, 8], [1, 2, 3], [2, 4, 4], [3, 4, 7], [0, 4, 10]]
    K = 40
    print(tourists(list, K))