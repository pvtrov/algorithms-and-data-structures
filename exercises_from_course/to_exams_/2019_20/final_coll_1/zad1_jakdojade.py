from math import inf
from queue import PriorityQueue
"""
Dana jest tablica dwuwymiarowa G, przedstawiająca macierz sąsiedztwa skierowanego grafu ważonego, który odpowiada mapie 
drogowej (wagi przedstawiają odległości, liczba -1 oznacza brak krawędzi). W niektórych wierzchołkach są stacje paliw, 
podana jest ich lista P. Pełnego baku wystarczy na przejechanie odległości d. Wjeżdżając na stację samochód zawsze jest 
tankowany do pełna.
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
from zad1testy import runtests

# nie dziala przekazywanie sciezki

def get_result(parents, graph, point, road, vertex, stations):
    stop = parents[point][vertex]
    if stop == -1:
        return road
    if stop in stations:
        point = len(parents)-1
    else:
        val = graph[stop][point]
        point += val
    road = get_result(parents, graph, point, road, stop, stations)
    road.append(stop)
    return road


def jak_dojade(graph, stations, full, start, destination):
    n = len(graph)
    distance = [[inf] * n for _ in range(full+1)]
    parents = [[-1] * n for _ in range(full+1)]
    pq = PriorityQueue()

    for i in range(full+1):
        distance[i][start] = 0
    pq.put((0, start, full))

    while not pq.empty():
        d, vertex, current = pq.get()
        if vertex == destination:
            continue
        for u in range(n):
            current_ = current
            if 0 < graph[vertex][u] <= current_:
                last = current_
                current_ -= graph[vertex][u]
                if u in stations:
                    current_ = full
                if distance[current_][u] > distance[last][vertex] + graph[vertex][u]:
                    distance[current_][u] = distance[last][vertex] + graph[vertex][u]
                    parents[current_][u] = vertex
                    pq.put((distance[current_][u], u, current_))

    min_ = inf
    point = None
    for c in range(n):
        if distance[c][destination] < min_:
            min_ = distance[c][destination]
            point = c

    if point is None:
        return -1

    road = get_result(parents, graph, point, [], destination, stations)

    return [min_]
        

runtests( jak_dojade )
# G = [[-1, 6,-1, 5, 2],
#      [-1,-1, 1, 2,-1],
#      [-1,-1,-1,-1,-1],
#      [-1,-1, 4,-1,-1],
#      [-1,-1, 8,-1,-1]]
# P = [0,1,3]
# print(jak_dojade(G, P, 3, 0, 2))