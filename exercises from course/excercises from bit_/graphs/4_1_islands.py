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
Przykład Dla tablicy
G1 = [ [0,5,1,8,0,0,0 ],
[5,0,0,1,0,8,0 ],
[1,0,0,8,0,0,8 ],
[8,1,8,0,5,0,1 ],
[0,0,0,5,0,1,0 ],
[0,8,0,0,1,0,5 ],
[0,0,8,1,0,5,0 ] ]
funkcja islands(G1, 5, 2) powinna zwrócić wartość 13
"""
from math import inf
from queue import PriorityQueue


def islands(graph, start, destination):
    n = len(graph)
    distance = [inf for _ in range(n)]
    parent = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]
    pq = PriorityQueue()
    distance[start] = 1
    visited[start] = True
    last_mode = 0

    for i in range(n):
        pq.put((distance[i], i))
    while not pq.empty():
        d, vertex = pq.get()
        if vertex == destination:
            return distance[destination]
        for u in range(n):
            if graph[vertex][u] != 0 and visited[u] is False and graph[vertex][u] != last_mode:
                if distance[vertex] + graph[vertex][u] < distance[u]:
                    distance[u] = distance[vertex] + graph[vertex][u]
                    parent[u] = vertex
                    last_mode = graph[vertex][u]
                    pq.put((distance[u], u))


G1 = [[0, 5, 1, 8, 0, 0, 0],
      [5, 0, 0, 1, 0, 8, 0],
      [1, 0, 0, 8, 0, 0, 8],
      [8, 1, 8, 0, 5, 0, 1],
      [0, 0, 0, 5, 0, 1, 0],
      [0, 8, 0, 0, 1, 0, 5],
      [0, 0, 8, 1, 0, 5, 0]]

print(islands(G1, 0, 5))
