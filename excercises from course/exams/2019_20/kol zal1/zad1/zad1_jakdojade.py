
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


def print_path(parent, i, result):
    if parent[i] == -1:
        result.append(i)
        return result
    result = print_path(parent, parent[i], result)
    result.append(i)
    return result


def jakdojade(graph, stations, max_capacity, start, destination):
    n = len(graph)
    # actual_capacity = max_capacity
    distance = [inf for _ in range(n)]
    parent = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]
    actual_capacity = [0 for _ in range(n)]
    visited[start] = True
    pq = PriorityQueue()
    distance[start] = 1
    actual_capacity[start] = max_capacity

    for i in range(n):
        pq.put((distance[i], i))
    while not pq.empty():
        d, vertex = pq.get()
        if vertex == destination:
            result = print_path(parent, destination, [])
            if len(result) == 1 and result[0] == destination:
                return -1
            else:
                return result

        for u in range(n):
            if 0 < graph[vertex][u] <= actual_capacity[vertex] and not visited[u]:
                if distance[vertex] + graph[vertex][u] <= distance[u]:
                    distance[u] = distance[vertex] + graph[vertex][u]
                    parent[u] = vertex
                    if u in stations:
                        actual_capacity[u] = max_capacity
                    else:
                        actual_capacity[u] = actual_capacity[vertex] - graph[vertex][u]
                    pq.put((distance[u], u))


runtests( jakdojade )
