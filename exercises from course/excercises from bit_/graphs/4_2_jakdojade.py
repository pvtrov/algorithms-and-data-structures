"""
Dana jest tablica dwuwymiarowa G, przedstawiająca macierz sąsiedztwa skierowanego grafu ważonego, który odpowiada mapie
drogowej (wagi przedstawiają odległości, liczba -1 oznacza brak
krawędzi). W niektórych wierzchołkach są stacje paliw, podana jest ich lista P. Pełnego baku wystarczy na przejechanie
odległości d. Wjeżdżając na stację samochód zawsze jest tankowany do pełna.
Proszę zaimplemntować funkcję jak dojade(G, P, d, a, b), która szuka najkrótszej możliwej
trasy od wierzchołka a do wierzchołka b, jeśli taka istnieje, i zwraca listę kolejnych odwiedzanych
na trasie wierzchołków (zakładamy, że w a też jest stacja paliw; samochód może przejechać najwyżej
odległość d bez tankowania).
Zaproponowana funkcja powinna być możliwe jak najszybsza. Uzasadnij jej poprawność i oszacuj
złożoność obliczeniową.
Przykład Dla tablic
G = [[-1, 6,-1, 5, 2],
[-1,-1, 1, 2,-1],
[-1,-1,-1,-1,-1],
[-1,-1, 4,-1,-1],
[-1,-1, 8,-1,-1]]
P = [0,1,3]
funkcja jak dojade(G, P, 5, 0, 2) powinna zwrócić [0,3,2]. Dla tych samych tablic funkcja
jak dojade(G, P, 6, 0, 2) powinna zwrócić [0,1,2], natomiast jak dojade(G, P, 3, 0, 2)
powinna zwrócić None.
"""
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
                return None
            else:
                return result

        for u in range(n):
            if 0 < graph[vertex][u] <= actual_capacity[vertex] and not visited[u]:
                if distance[vertex] + G[vertex][u] < distance[u]:
                    distance[u] = distance[vertex] + graph[vertex][u]
                    parent[u] = vertex
                    if u in stations:
                        actual_capacity[u] = max_capacity
                    else:
                        actual_capacity[u] = actual_capacity[vertex] - graph[vertex][u]
                    pq.put((distance[u], u))


G = [[-1, 6, -1, 5, 2],
     [-1, -1, 1, 2, -1],
     [-1, -1, -1, -1, -1],
     [-1, -1, 4, -1, -1],
     [-1, -1, 8, -1, -1]]
P = [0, 1, 3]
print(jakdojade(G, P, 6, 0, 2))
