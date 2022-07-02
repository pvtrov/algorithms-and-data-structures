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

"""
jednak troche zly algorytm XD i nie dziala dobrze
"""

def print_path(parent, i, result):
    if parent[i] == -1:
        result.append(i)
        return result
    result = print_path(parent, parent[i], result)
    result.append(i)
    return result


def jak_dojade(graph, stations, max_capacity, start, destination):
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
                if distance[vertex] + graph[vertex][u] < distance[u]:
                    distance[u] = distance[vertex] + graph[vertex][u]
                    parent[u] = vertex
                    if u in stations:
                        actual_capacity[u] = max_capacity
                    else:
                        actual_capacity[u] = actual_capacity[vertex] - graph[vertex][u]
                    pq.put((distance[u], u))



# TESTY ###########################################################################

import copy

G1 = [[-1, 5, -1, 2], [-1, -1, -1, -1], [5, -1, -1, 5], [2, 2, -1, -1]]
P1 = [2, 0]
L1 = 9
# a=2, b=1, d=6

G2 = [[-1, 2, -1, -1, 3], [2, -1, 2, -1, -1], [-1, 2, -1, 2, -1], [-1, -1, 2, -1, 3], [3, -1, -1, 3, -1]]
P2 = [0, 2]
L2 = 6
# a=0, b=3, d=4

G3 = [[-1, 3, -1, 5, -1, 2], [3, -1, 4, -1, -1, -1], [-1, 4, -1, 6, -1, -1], [-1, -1, 6, -1, 2, -1],
      [-1, 5, -1, 2, -1, 3], [2, -1, -1, -1, 3, -1]]
P3 = [0, 4, 5]
L3 = -1
# a=5, b=2, d=5


TESTS = [(G1, P1, 6, 2, 1, L1),
         (G2, P2, 4, 0, 3, L2),
         (G3, P3, 5, 5, 2, L3)]


def isok(G, P, d, a, b, path, exp_len):
    if exp_len < 0 and path == None:
        print("Brak sciezki, zgodnie z oczekiwaniem")
        return True
    if exp_len >= 0 and path == None:
        print("Rozwiazanie nie zwrocilo sciezki, mimo ze taka istnieje")
        return False

    if path[0] != a:
        print("Rozwiazanie zwraca bledny poczatek sciezki")

    tank = d
    sol_len = 0
    v = a
    for u in path[1:]:
        if G[v][u] < 0:
            print("Nie istnieje krawedz z %d to %d" % (v, u))
            return False
        tank -= G[v][u]
        sol_len += G[v][u]
        if tank < 0:
            print("Zabraklo benzyny na krawedzi z %d do %d" % (v, u))
            return False
        v = u
        if v in P:
            tank = d

    print("Dlugosc otrzymanej trasy =", sol_len)
    if sol_len > exp_len:
        print("Za dluga trasa!")
        return False

    return True


def runtests(f):
    OK = True
    for (G, P, d, a, b, L) in TESTS:
        res = f(copy.deepcopy(G), copy.deepcopy(P), d, a, b)
        print("----------------------")
        print("G =")
        for i in range(len(G)): print(G[i])
        print("P =", P)
        print("d = ", d)
        print("a = ", a)
        print("b = ", b)
        print("otrzymany wynik  =", res)
        print("oczekiwana dlugosc trasy =", L)

        if not isok(G, P, d, a, b, res, L):
            print("Blad!")
            OK = False
        else:
            print()
    print("----------------------")

    if OK:
        print("OK!")
    else:
        print("Bledy!")

runtests(jak_dojade)

