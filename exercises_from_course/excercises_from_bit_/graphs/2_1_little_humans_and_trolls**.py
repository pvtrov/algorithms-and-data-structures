"""
Wyobraźmy sobie podziemny labirynt, złożony z ogromnych jaskiń połączonych wąskimi korytarzami.
W jednej z jaskiń krasnoludy zbudowały swoją osadę, a w każdej z pozostałych jaskiń mieszka znana krasnoludom ilość
trolli. Krasnoludy chcą zaplanować swoją obronę na wypadek ataku ze strony trolli. Zamierzają w tym celu zakraść się i
podłożyć ładunek wybuchowy pod jeden z korytarzy, tak aby trolle mieszkające za tym korytarzem nie miały żadnej ścieżki,
którą mogłyby dotrzeć do osady krasnoludów.
Który korytarz należy wysadzić w powietrze, aby odciąć dostęp do krasnoludzkiej osady największej liczbie trolli?
"""

"""
znajdujemy wszytskie mosty, odsiewamy te które są dostepne z jaskini krasnoludów bez przechodzenia przez inne mosty,
potem zliczamy ilosc trolli po drugiej stronie mostu i wysadzamy odpowiedni
"""


class vert:
    def __init__(self):
        self.visited = False
        self.d = -1
        self.low = -1
        self.parent = -1


def DFSb(G, v, nr, vertices, result):
    vertices[v].visited = True
    nr += 1
    vertices[v].d = vertices[v].low = nr
    for w in G[v]:
        if not vertices[w].visited:
            vertices[w].parent = v
            nr, vertices, result = DFSb(G, w, nr, vertices, result)
            vertices[v].low = min(vertices[v].low, vertices[w].low)
            if vertices[w].low == vertices[w].d:
                result.append((w, vertices[w].parent))
        elif w != vertices[v].parent:
            vertices[v].low = min(vertices[v].low, vertices[w].d)
    return nr, vertices, result


def bridge(G):
    n = len(G)
    vertices = [vert() for _ in range(n)]
    nr = 0
    result = []
    for u in range(len(G)):
        if not vertices[u].visited:
            nr, vertices, result = DFSb(G, u, nr, vertices, result)

    return result


def select_bridges(graph, start, bridges):

    return []


def bum(graph, trolls, k):
    bridges = bridge(graph)
    good_bridges = select_bridges(graph, k, bridges)
    return bridges


trolls = [5, 10, -1, 11, 12, 14, 10]
graph = [[1],
         [0, 2],
         [1, 4],
         [4],
         [3, 2, 6, 5],
         [4, 6],
         [4, 5]]
k = 2

print(bum(graph, trolls, k))