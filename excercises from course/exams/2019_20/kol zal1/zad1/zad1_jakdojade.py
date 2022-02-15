
from zad1testy import runtests

# Dana jest tablica dwuwymiarowa G, przedstawiająca macierz sąsiedztwa skierowanego grafu ważonego, który odpowiada
# mapie drogowej (wagi przedstawiają odległości, liczba -1 oznacza brak
# krawędzi). W niektórych wierzchołkach są stacje paliw, podana jest ich lista P.
# Pełnego baku wystarczy na przejechanie odległości d. Wjeżdżając na stację samochód zawsze jest tankowany do pełna.
# Proszę zaimplemntować funkcję jak dojade(G, P, d, a, b), która szuka najkrótszej możliwej
# trasy od wierzchołka a do wierzchołka b, jeśli taka istnieje, i zwraca listę kolejnych odwiedzanych
# na trasie wierzchołków (zakładamy, że w a też jest stacja paliw; samochód może przejechać najwyżej
# odległość d bez tankowania).
# Zaproponowana funkcja powinna być możliwe jak najszybsza. Uzasadnij jej poprawność i oszacuj
# złożoność obliczeniową.

# gdzies jest błąd i zbieram sie zeby go znaleźć

from math import inf
from queue import PriorityQueue


def path(parent, start, end):
    helper = end
    road = []
    while helper != start:
        if helper == -1:
            return None
        road.append(helper)
        helper = parent[helper]
    road.append(start)
    return road[::-1]


def jak_dojade(graph, stations, capacity, start, end):
    full_capacity = capacity
    length = len(graph)
    distance = [inf for _ in range(length)]
    parent = [-1 for _ in range(length)]
    visited = [False for _ in range(length)]
    distance[start] = 0
    visited[start] = True
    fuel = [0 for _ in range(length)]
    fuel[start] = capacity
    queueueueue = PriorityQueue()
    queueueueue.put((distance[start], start))

    for i in range(length):
        queueueueue.put((distance[i], i))

    while not queueueueue.empty():
        road, vertex = queueueueue.get()
        if vertex == end:
            return path(parent, start, end)

        for u in range(length):
            if graph[vertex][u] != -1 and graph[vertex][u] <= fuel[vertex]:
                if distance[vertex] + graph[vertex][u] <= distance[u]:
                    distance[u] = distance[vertex] + graph[vertex][u]
                    parent[u] = vertex
                    if u in stations:
                        fuel[u] = full_capacity
                    else:
                        fuel[u] = fuel[vertex] - graph[vertex][u]
                    queueueueue.put((distance[u], u))

    return path(parent, start, end)


runtests( jak_dojade ) 
