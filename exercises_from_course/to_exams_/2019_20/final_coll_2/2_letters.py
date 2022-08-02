"""
Dany jest graf nieskierowany G = (V, E), gdzie każdy wierzchołek z V ma przypisaną małą literę z
alfabetu łacińskiego, a każda krawędź ma wagę (dodatnią liczbę całkowitą). Dane jest także słowo
W = W[0], . . . ,W[n − 1] składające się małych liter alfabetu łacińskiego. Należy zaimplementować
funkcję letters(G,W), która oblicza długość najkrótszej ścieżki w grafie G, której wierzchołki
układają się dokładnie w słowo W (ścieżka ta nie musi być prosta i może powtarzać wierzchołki).
Jeśli takiej ścieżki nie ma, należy zwrócić -1.
Struktury danych. Graf G ma n wierzchołków ponumerowanych od 0 do n − 1 i jest reprezentowany jako para (L, E). L to
lista o długości n, gdzie L[i] to litera przechowywana w wierzchołku
i. E jest listą krawędzi i każdy jej element jest trójką postaci (u, v, w), gdzie u i v to wierzchołki
połączone krawędzią o wadze w.
"""
"""
gdzies jest blad w implementacji
"""

from math import inf
from queue import PriorityQueue

letters_table = ["k", "k", "o", "o", "t", "t"]


def dijkstra(graph, start, word):
    distances = [inf] * len(graph)
    last_letters = [-1] * len(graph)
    last_letters[start] = 0
    pq = PriorityQueue()
    pq.put((0, start))

    while not pq.empty():
        value, vertex = pq.get()
        for i in graph[vertex]:
            if last_letters[vertex] + 1 < len(word):
                if letters_table[i[0]] == word[last_letters[vertex] + 1] and distances[i[0]] > value + i[1]:
                    distances[i[0]] = value + i[1]
                    last_letters[i[0]] = last_letters[vertex] + 1
                    pq.put((distances[i[0]], i[0]))

    return distances


def make_me_graph(almost):
    maks = -1
    for i in range(len(almost)):
        if almost[i][0] > maks:
            maks = almost[i][0]
        if almost[i][1] > maks:
            maks = almost[i][1]

    graph = [[] for _ in range(maks+1)]
    for edge in almost:
        graph[edge[0]].append([edge[1], edge[2]])
        graph[edge[1]].append([edge[0], edge[2]])
    return graph


def letters(almost_graph, word):
    graph = make_me_graph(almost_graph)
    start_ver = []
    end_ver = []
    minimum_from_all = []

    for i in range(len(graph)):
        if letters_table[i] == word[0]:
            start_ver.append(i)
        if letters_table[i] == word[-1]:
            end_ver.append(i)

    for i in range(len(start_ver)):
        distances = dijkstra(graph, start_ver[i], word)
        mini = min(distances[end_ver[j]] for j in range(len(end_ver)))
        minimum_from_all.append(mini)

    if min(minimum_from_all) == inf:
        return -1
    return min(minimum_from_all)


E = [(0,2,2), (1,2,1), (1,4,3), (1,3,2), (2,4,5), (3,4,1), (3,5,3) ]
print(letters(E, "kokot"))