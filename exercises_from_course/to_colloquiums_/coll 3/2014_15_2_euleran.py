"""
Dana jest struktura danych:

struct Edge {
int u, v; // u < v
Edge* next;
};

Napisz funkcję bool Euleran( Edge* E, int n ), która sprawdza czy graf zadany przez listę
krawędzi posiada cykl Eulera (n to liczba wierzchołków w grafie). Graf jest nieskierowany
i spójny. Krawędzie w liście mogą się powtarzać. Funkcja powinna alokować nie więcej pamięci,
niż liniowo proporcjonalnie do ilości krawędzi.
"""


class Edge:
    def __init__(self, u, v):
        self.u = u
        self.v = v
        self.next = None


def DFS(u, graph, deleted, cycle, vertex_counter):
    for v in graph[u]:      # przechodze po sasiadach
        if deleted[u][v] is False:      # jesli nie krawedz jest nie usunieta to ja usuwam
            deleted[u][v] = True
            deleted[v][u] = True
            cycle = DFS(v, graph, deleted, cycle, vertex_counter)
            cycle.append(u)
            if u not in vertex_counter:
                vertex_counter.append(u)
    return cycle


def tab_to_list(array):
    h = array[0]
    c = h
    for i in range(1, len(array)):
        x = array[i]
        c.next = x
        c = x

    return h.next


def euler(graph):
    for i in range(len(graph)):  # sprawdzam czy moze byc cykl
        if len(graph[i]) == 0 or len(graph[i]) % 2 != 0:
            return None

    deleted = [[False for _ in range(len(graph))] for _ in range(len(graph))] # macierz usunietych krawedzi
    cycle = [0]             # odpoweidnie wierzchołki cyklu
    vertex_counter = []         # użyte wierzchołki, pomoze w stwerdzeniu czy graf jest spojny
    cycle = DFS(0, graph, deleted, cycle, vertex_counter)
    if len(vertex_counter) != len(graph):   # jeśli liczba wierzchołkow w cyklu jest inna od liczby wierzchlkow w grafie
        return None                         # oznacza ze graf jest niespojny
    return cycle


def make_graph(edge, n):
    graph = [set() for _ in range(n)]

    while edge is not None:
        graph[edge.u].add(edge.v)
        graph[edge.v].add(edge.u)
        edge = edge.next

    return graph


def euleran(edge, n):
    graph = make_graph(edge, n)
    cycle = euler(graph)
    if len(cycle) > 0:
        return True
    return False


edges = [Edge(0, 1), Edge(2, 3), Edge(1, 3), Edge(0, 2), Edge(3, 4), Edge(4, 5), Edge(3, 4), Edge(1, 0), Edge(3, 5)]
edge = tab_to_list(edges)
print(euleran(edge, 6))