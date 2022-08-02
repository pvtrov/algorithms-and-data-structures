"""
Na tablicach w kantorze wisi lista trójek (waluta1, waluta2, kurs). Każda z takich trójek oznacza,
że kantor kupi n waluty2 za kurs*n waluty1.
Znajdź najkorzystniejszą sekwencję wymiany waluty A na walutę B
Czy istnieje taka sekwencja wymiany walut, która zaczyna się i kończy w tej samej walucie i kończymy z większą
ilością pieniędzy niż zaczynaliśmy?
"""
'Przechodzę na logarytmy i sprawdzam czy istnieje cykl ujemny, jeśli isteniej to oznacza, że można uzyskać więcej przez ' \
'wymianę'

from math import inf, log2


def make_graph(currencies):
    size = -1
    for i in range(len(currencies)):
        if currencies[i][0] > size:
            size = currencies[i][1]
        elif currencies[i][1] > size:
            size = currencies[i][1]

    graph = [[] for _ in range(size + 1)]
    for i in range(len(currencies)):
        graph[currencies[i][0]].append([currencies[i][1], log2(currencies[i][2])])

    return graph


def relax(graph, u, v, distance, parent):
    if distance[graph[u][v][0]] > distance[u] + graph[u][v][1]:
        distance[graph[u][v][0]] = distance[u] + graph[u][v][1]
        parent[graph[u][v][0]] = u


def Bellman_Ford(graph, start):
    distance = [inf for _ in range(len(graph))]
    parent = [None for _ in range(len(graph))]
    distance[start] = 0

    for u in range(len(graph)-1):
        for v in range(len(graph[u])):
            relax(graph, u, v, distance, parent)

    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if distance[graph[i][j][0]] > distance[i] + graph[i][j][1]:
                return True
    return False


def currency_exchange(currencies, start_money, start_currency):
    graph = make_graph(currencies)
    return Bellman_Ford(graph, start_currency)


currencies = [[0, 1, 5], [0, 2, 6], [1, 2, 6], [0, 3, 4], [2, 3, 3], [1, 3, 6], [1, 0, 4], [2, 0, 4], [2, 1, 7],
              [3, 0, 3], [3, 2, 2], [3, 1, 4]]
print(currency_exchange(currencies, 50, 0))





