# W pewnym państwie, w którym znajduje się N miast, postanowiono połączyć
# wszystkie miasta siecią autostrad, tak aby możliwe było dotarcie autostradą do każdego miasta. Ponieważ
# kontynent, na którym leży państwo jest płaski położenie każdego z miast opisują dwie liczby x, y, a odległość
# w linii prostej pomiędzy miastami liczona w kilometrach wyraża się wzorem len =
# √((x1 − x2)^2 + (y1 − y2)^2).
# Z uwagi na oszczędności materiałów autostrada łączy dwa miasta w linii prostej.
# Ponieważ zbliżają się wybory prezydenta, wszystkie autostrady zaczęto budować równocześnie i jako cel
# postanowiono zminimalizować czas pomiędzy otwarciem pierwszej i ostatniej autostrady. Czas budowy autostrady
# wyrażony w dniach wynosi ⌈len⌉ (sufit z długości autostrady wyrażonej w km). Proszę zaproponować
# algorytm wyznaczający minimalną liczbę dni dzielącą otwarcie pierwszej i ostatniej autostrady


"""
1. Obliczamy minimalne drzewo rozpinające
2. Odejmujemy od siebie max i min wartość, stąd mamy minimalną ilość dni pomiedzy otwarciem
"""
from math import ceil, inf, sqrt


class Node:
    def __init__(self, val):
        self.val = val
        self.rank = 0
        self.parent = self


def find(x):
    if x != x.parent:
        x.parent = find(x.parent)
    return x.parent


def union(x, y):
    x = find(x)
    y = find(y)

    if x == y: return
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


def kruskal(G):
    n = len(G)
    edges = []
    t = []
    for i in range(n):
        for j in range(i, n):
            if G[i][j] != 0:
                t.append((G[i][j], i, j))
    t.sort(key=lambda t: t[0])

    for i in range(n):
        edges.append(Node(i))

    A = []
    weight = 0
    for edge in range(n):
        v = edges[t[edge][1]]
        u = edges[t[edge][2]]
        if not find(v) is find(u):  # czy v i u leżą w innych składowych grafu
            union(v, u)  # łaczymy zbiory
            A.append((v.val, u.val))
            weight += t[edge][0]

    min_val = inf
    max_val = -inf
    for i in A:
        min_val = min(G[i[0]][i[1]], min_val)
        max_val = max(G[i[0]][i[1]], max_val)

    min_difference = abs(max_val-min_val)
    return min_difference


def create_graph(almost_graph):
    graph = [[0 for _ in range(len(almost_graph))] for _ in range(len(almost_graph))]
    counter = 0
    for vertex in almost_graph:
        helper = 0
        for neighbour in almost_graph:
            if vertex != neighbour:
                length = ceil(sqrt((neighbour[1]-vertex[1])**2 + (neighbour[0]-vertex[0])**2))
                graph[counter][helper] = length
                graph[helper][counter] = length
            helper += 1
        counter += 1
    return graph


def highways(cities):
    graph = create_graph(cities)
    return kruskal(graph)


cities = [(0, 1), (3, 4), (6, 2), (4, 0)]
print(highways(cities))