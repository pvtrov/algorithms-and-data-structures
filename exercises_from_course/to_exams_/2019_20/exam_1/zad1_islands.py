from math import inf
from queue import PriorityQueue

from zad1testy import runtests
"""
Pewna kraina składa się z wysp pomiędzy którymi istnieją połączenia lotnicze, promowe oraz mosty.
Pomiędzy dwoma wyspami istnieje co najwyżej jeden rodzaj połączenia. Koszt przelotu z wyspy
na wyspę wynosi 8B, koszt przeprawy promowej wynosi 5B, za przejście mostem trzeba wnieść
opłatę 1B. Poszukujemy trasy z wyspy A na wyspę B, która na kolejnych wyspach zmienia środek
transportu na inny oraz minimalizuje koszt podróży.
Dana jest tablica G, określająca koszt połączeń pomiędzy wyspami. Wartość 0 w macierzy
oznacza brak bezpośredniego połączenia. Proszę zaimplementować funkcję islands( G, A, B )
zwracającą minimalny koszt podróży z wyspy A na wyspę B. Jeżeli trasa spełniająca warunki zadania
nie istnieje, funkcja powinna zwrócić wartość None.
"""


def islands(G, A, B):
    costs = [inf for _ in range(len(G))]
    parents = [-1] * len(G)
    last_options = [None] * len(G)
    visited = [False] * len(G)
    pq = PriorityQueue()
    costs[A] = 0
    visited[A] = True

    for i in range(len(G)):
        pq.put((costs[i], i))
    while not pq.empty():
        cost, city = pq.get()
        if city == B:
            return costs[B]
        for neighbour in range(len(G)):
            if G[city][neighbour] != 0 and not visited[neighbour] and G[city][neighbour] != last_options[city]:
                if costs[city] + G[city][neighbour] < costs[neighbour]:
                    costs[neighbour] = costs[city] + G[city][neighbour]
                    parents[neighbour] = city
                    last_options[neighbour] = G[city][neighbour]
                    pq.put((costs[neighbour], neighbour))
    return None
        

runtests( islands ) 
