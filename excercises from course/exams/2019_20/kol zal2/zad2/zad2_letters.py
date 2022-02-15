from zad2testy import runtests
from queue import Queue, PriorityQueue
from math import inf

"""
Dany jest graf nieskierowany G = (V, E), gdzie każdy wierzchołek z V ma przypisaną małą literę z
alfabetu łacińskiego, a każda krawędź ma wagę (dodatnią liczbę całkowitą). Dane jest także słowo
W = W[0], . . . ,W[n − 1] składające się małych liter alfabetu łacińskiego. Należy zaimplementować
funkcję letters(G,W), która oblicza długość najkrótszej ścieżki w grafie G, której wierzchołki
układają się dokładnie w słowo W (ścieżka ta nie musi być prosta i może powtarzać wierzchołki).
Jeśli takiej ścieżki nie ma, należy zwrócić -1.
Struktury danych. Graf G ma n wierzchołków ponumerowanych od 0 do n − 1 i jest reprezentowany jako para (L, E). 
L to lista o długości n, gdzie L[i] to litera przechowywana w wierzchołku i. E jest listą krawędzi i każdy jej element 
jest trójką postaci (u, v, w), gdzie u i v to wierzchołki połączone krawędzią o wadze w.
"""
"""
najpierw robie zwykly grap, potem odpalam dijsktre, z tym relaksuje tylko te wierzcholki które pasuja do aktualnej litery
 oraz zmieniam troche sposob zapisu wyniku
 złożoność czasowa: O( E + VElogV )
 """


def make_graph(G):
    E = G[1]
    graph = [[] for _ in range(len(G[0]))]
    for i in E:
        graph[i[0]].append((i[1], i[2]))
        graph[i[1]].append((i[0], i[2]))

    return graph


def split(word):
    return list(word)


def weird_dijkstra(graph, letters, start, word):
    length = len(graph)
    values = [inf] * length
    values[start] = 0
    result = [inf] * length
    index = 0
    p_queue = PriorityQueue()
    p_queue.put((0, start, index))

    while not p_queue.empty():
        val, prev, index = p_queue.get()
        if index+1 < len(word):
            for i in graph[prev]:
                if letters[i[0]] == word[index+1]:
                    values[i[0]] = val + i[1]
                    if index + 1 == len(word)-1:
                        if result[i[0]] > val + i[1]:
                            result[i[0]] = val + i[1]
                    else:
                        p_queue.put((values[i[0]], i[0], index+1))
                else:
                    values[i[0]] = inf

    return min(result)


def letters( G, W ):
    letters = G[0]
    word = split(W)
    true_graph = make_graph(G)
    vertex_to_start = Queue()

    for i in range(len(letters)):
        if word[0] == letters[i]:
            vertex_to_start.put(i)

    min_cost = inf
    while vertex_to_start.qsize():
        start = vertex_to_start.get()
        temp_min_cost = weird_dijkstra(true_graph, letters, start, word)
        if min_cost > temp_min_cost > 0:
            min_cost = temp_min_cost

    if min_cost == inf:
        return -1

    return min_cost
    

runtests( letters )
    
    
