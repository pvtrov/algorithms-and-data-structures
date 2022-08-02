import copy
from math import inf, ceil, sqrt

from zad2testy import runtests
"""
W pewnym państwie, w którym znajduje się N miast, postanowiono połączyć wszystkie miasta siecią autostrad, tak aby 
możliwe było dotarcie autostradą do każdego miasta. Ponieważ kontynent, na którym leży państwo jest płaski położenie 
każdego z miast opisują dwie liczby x, y, a odległość w linii prostej pomiędzy miastami liczona w kilometrach wyraża 
się wzorem len =√(x1 − x2)**2 + (y1 − y2)**2. Z uwagi na oszczędności materiałów autostrada łączy dwa miasta w linii 
prostej. Ponieważ zbliżają się wybory prezydenta, wszystkie autostrady zaczęto budować równocześnie
i jako cel postanowiono zminimalizować czas pomiędzy otwarciem pierwszej i ostatniej autostrady.
Czas budowy autostrady wyrażony w dniach wynosi ⌈len⌉ (sufit z długości autostrady wyrażonej w km).
Proszę zaimplementować funkcję highway(A), która dla danych położeń miast wyznacza minimalną liczbę dni dzielącą 
otwarcie pierwszej i ostatniej autostrady.
"""

"""
jako ze najmniejsza róznaica jest w takim przedziale gdzie jest n-1 "najblizszych" sobie liczb to szukam takiego
minimalnego drzewa rozpinajacego ze roznica w danych przedziale n-1 liczb jest najmnijesza: 
1.tak jak w kruskalu umieszczam krawedzie w kolejce priorytetowej
2.szukam MST zaczynajac od najkrótszej krawedzi, zapisuje róznice max długosci i min długosci
3. nastepnie znowu szukam MST tylko zaczynajac od przednajkrótszej krawedzi, aktualizjac minimalna róznice
 i tak az zosatnie mi w kolejce n-1 krawedzi
 
złożność czasowa: O( (E-(n-1)) * ElogE ) gdzie E to liczba krawedzi powstałego grafu
pamieciowa: O(n^2)

"""

class Node:
    def __init__(self, value):
        self.val = value
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


def remove_edge_in_kruskal(graph, u, v):
    graph[graph[u][v][0]].remove((u, graph[u][v][1]))


def remove_edge(graph, i, j, weight):
    graph[i].remove((j, weight))
    graph[j].remove((i, weight))


def count_distance(x1, x2, y1, y2):
    return ceil(sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))


def get_graph(A, graph):
    for i in range(len(A)):
        for j in range(len(A)):
            if i != j:
                distance = count_distance(A[i][0], A[j][0], A[i][1], A[j][1])
                graph[i].append((j, distance))
    return graph


def kruskal(graph):
    length = len(graph)
    edges = []
    sorted_edges = []

    for i in range(length):
        for j in range(len(graph[i])):
            sorted_edges.append((graph[i][j][1], i, graph[i][j][0]))
            remove_edge_in_kruskal(graph, i, j)
    sorted_edges.sort(key=lambda sorted_edges: sorted_edges[0])
    to_remove = sorted_edges[0]

    for i in range(length):
        edges.append(Node(i))

    min_time = inf
    max_time = -inf

    for edge in range(length):
        v = edges[sorted_edges[edge][1]]
        u = edges[sorted_edges[edge][2]]
        if not find(v) is find(u):
            union(v, u)
            if sorted_edges[edge][0] < min_time:
                min_time = sorted_edges[edge][0]
            elif sorted_edges[edge][0] > max_time:
                max_time = sorted_edges[edge][0]

    return to_remove, max_time - min_time


def highway(A):
    if len(A) == 2:
        return 0

    graph = [[] for _ in range(len(A))]
    graph = get_graph(A, graph)
    min_time = inf

    for i in range(len(graph) - 1):
        to_kruskal_graph = copy.deepcopy(graph)
        to_remove, result = kruskal(to_kruskal_graph)
        remove_edge(graph, to_remove[1], to_remove[2], to_remove[0])
        if min_time > result:
            min_time = result

    return min_time


runtests( highway ) 
