from zad1testy import runtests as xd

"""
Pewna kraina składa się z wysp pomiędzy którymi istnieją połączenia lotnicze, promowe oraz mosty.
Pomiędzy dwoma wyspami istnieje co najwyżej jeden rodzaj połączenia. Koszt przelotu z wyspy
na wyspę wynosi 8B, koszt przeprawy promowej wynosi 5B, za przejście mostem trzeba wnieść
opłatę 1B. Poszukujemy trasy z wyspy A na wyspę B, która na kolejnych wyspach zmienia środek
transportu na inny oraz minimalizuje koszt podróży.
Dana jest tablica G, określająca koszt połączeń pomiędzy wyspami. Wartość 0 w macierzy
oznacza brak bezpośredniego połączenia. Proszę zaimplementować funkcję islands( G, A, B )
zwracającą minimalny koszt podróży z wyspy A na wyspę B. Jeżeli trasa spełniająca warunki zadania
nie istnieje, funkcja powinna zwrócić wartość None."""


"""
odpalam zmodyfikowana dijkstre, relaksując tylko wierzchołki spełniające założenie o tym że musi byc inny sposob wydostania z 
wierzchołka
"""

from math import inf
from queue import PriorityQueue



def islands(G, A, B):
    number_of_islands = len(G)
    distance = [inf for _ in range(number_of_islands)]
    parents = [-1 for _ in range(number_of_islands)]
    visited = [False for _ in range(number_of_islands)]
    visited[A] = True
    queueueueueueueuue = PriorityQueue()
    distance[A] = 0
    prev_val = [-1 for _ in range(number_of_islands)]

    for i in range(number_of_islands):
        queueueueueueueuue.put((distance[i], i))

    while not queueueueueueueuue.empty():
        d, v = queueueueueueueuue.get()
        if v == B:
            return distance[B]

        for u in range(number_of_islands):
            if G[v][u] != 0 and G[v][u] != prev_val[v] and visited[u] is False:
                if distance[v] + G[v][u] < distance[u]:
                    distance[u] = distance[v] + G[v][u]
                    parents[u] = v
                    queueueueueueueuue.put((distance[u], u))
    return None

# G1 = [[0, 5, 1, 8, 0, 0, 0],
#       [5, 0, 0, 1, 0, 8, 0],
#       [1, 0, 0, 8, 0, 0, 8],
#       [8, 1, 8, 0, 5, 0, 1],
#       [0, 0, 0, 5, 0, 1, 8],
#       [0, 8, 0, 0, 1, 0, 5],
#       [0, 0, 8, 1, 8, 5, 0]]
#
# print(islands(G1, 6, 4))


xd(islands)
