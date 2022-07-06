from math import inf

from zad1testy import runtests
"""
Każdy nieskierowany, spójny i acyckliczny graf G = (V, E) możemy traktować jako drzewo. Korzeniem tego drzewa może być 
dowolny wierzchołek v ∈ V . Napisz funkcję best root(L), która przyjmuje nieskierowany, spójny i acyckliczny graf G 
(reprezentowany w postaci listy sąsiedztwa) i wybiera taki jego wierzchołek, by wysokość zakorzenionego w tym 
wierzchołku drzewa była możliwie najmniejsza. Jeśli kilka wierzchołków spełnia warunki zadania, funkcja może zwrócić 
dowolny z nich. Wysokość drzewa definiujemy jako liczbę krawędzi od korzenia do najdalszego liścia. 
Uzasadnij poprawność zaproponowanego algorytmu i oszacuj jego złożoność obliczeniową.

Funkcja best root(L) powinna zwrócić numer wierzchołka wybranego jako korzeń. Wierzchołki
numerujemy od 0. Argumentem best root(L) jest lista postaci:
L = [l0,l1, . . . ,ln−1],
gdzie li to lista zawierająca numery wierzchołków będących sąsiadami i−tego wierzchołka. Można
przyjąć (bez weryfikacji), że lista opisuje graf spełniający warunki zadania. W szczególności, graf
jest spójny, acykliczny, oraz jeśli a ∈ lb to b ∈ la (graf jest nieskierowany)."""

""" 
od razu odrzucam liscie, i puszczam dfs od kazdego nie lisciowego wierzcholka
"""


def dfs_visit(graph, vertex, visited, counter, distances):
    visited[vertex] = True
    counter += 1
    for neib in graph[vertex]:
        if not visited[neib]:
            dfs_visit(graph, neib, visited, counter, distances)
    if len(graph[vertex]) == 1:
        distances[vertex] = counter


def dfs(graph, vertex):
    visited = [False] * len(graph)
    distnces = [0] * len(graph)
    dfs_visit(graph, vertex, visited, 0, distnces)

    return distnces


def best_root( L ):
    # tu proszę zaimplementować zadanie
    n = len(L)
    min_ = inf
    vert = None
    res = None
    for vertex in range(len(L)):
        if len(L[vertex]) > 1:
            distances = dfs(L, vertex)
            temp_counet = max(distances)
            if temp_counet < min_:
                min_ = temp_counet
                res = vertex

    return res


runtests( best_root ) 
