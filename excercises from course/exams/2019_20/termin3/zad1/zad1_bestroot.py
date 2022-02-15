from zad1testy import runtests
from queue import Queue
from math import inf

"""
Każdy nieskierowany, spójny i acyckliczny graf G = (V, E) możemy traktować jako drzewo. Korzeniem tego drzewa może być 
dowolny wierzchołek v ∈ V . Napisz funkcję best root(L), która przyjmuje nieskierowany, spójny i acyckliczny graf 
G (reprezentowany w postaci listy sąsiedztwa) i
wybiera taki jego wierzchołek, by wysokość zakorzenionego w tym wierzchołku drzewa była możliwie najmniejsza. 
Jeśli kilka wierzchołków spełnia warunki zadania, funkcja może zwrócić dowolny z
nich. Wysokość drzewa definiujemy jako liczbę krawędzi od korzenia do najdalszego liścia. Uzasadnij
poprawność zaproponowanego algorytmu i oszacuj jego złożoność obliczeniową.
Funkcja best root(L) powinna zwrócić numer wierzchołka wybranego jako korzeń. Wierzchołki
numerujemy od 0. Argumentem best root(L) jest lista postaci:
L = [l0,l1, . . . ,ln−1],
gdzie li to lista zawierająca numery wierzchołków będących sąsiadami i−tego wierzchołka. Można
przyjąć (bez weryfikacji), że lista opisuje graf spełniający warunki zadania. W szczególności, graf
jest spójny, acykliczny, oraz jeśli a ∈ lb to b ∈ la (graf jest nieskierowany). Nagłówek funkcji powinien
mieć postać:
def best_root(L):
"""
"""
gdy wierzcholek jest lisciem to nawet nie sprawdam jego odleglosci do innych lisci
dla pozostalych wierscholkow licze odleglosc i wybieram maks. z odległosci od danego wierzchołka ale ze wszytskich tych
maksów biore minimum
złożoność czasowa: O(K * (V+E)) gdzie K to liczba wierzochłków które nie są liściami
pamięciowa: O(n)
  """


def suming_edges_BFS(L, root):
    queue = Queue()
    counted = [False for _ in range(len(L))]
    distance = [-1 for _ in range(len(L))]

    distance[root] = 0
    counted[root] = True
    queue.put(root)

    while queue.qsize():
        u = queue.get()
        for neighbour in L[u]:
            if not counted[neighbour]:
                counted[neighbour] = True
                distance[neighbour] = distance[u] + 1
                queue.put(neighbour)

    return max(distance)


def best_root( L ):
    n = len(L)
    min_distance = inf
    result = None
    maybe_result = Queue()

    for i in range(n):
        if len(L[i]) > 1:
            maybe_result.put(i)

    while maybe_result.qsize():
        vertex = maybe_result.get()
        distance = suming_edges_BFS(L, vertex)
        if distance < min_distance:
            min_distance = distance
            result = vertex

    return result


runtests( best_root ) 
