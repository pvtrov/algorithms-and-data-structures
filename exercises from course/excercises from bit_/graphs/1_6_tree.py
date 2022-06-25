"""
Dostajemy na wejściu listę krawędzi drzewa (niekoniecznie binarnego!) oraz wyróżniony wierzchołek - korzeń. Każdy
wierzchołek tworzy swoje własne poddrzewo. Dla każdego wierzchołka, wyznacz ilość wierzchołków w jego poddrzewie.
"""


def add_edge(parent, child, graph):
    graph[parent].append(child)


def DFS_visit(graph, vertex, visited, parent, counter):
    visited[vertex] = True
    counter += 1
    for child in graph[vertex]:
        if not visited[child]:
            counter = DFS_visit(graph, child, visited, parent, counter)
    return counter


def DFS(graph, start):
    visited = [False for _ in range(len(graph))]
    parent = [-1 for _ in range(len(graph))]
    counter = 0
    counter = DFS_visit(graph, start, visited, parent, counter)
    return counter


def count_sub_tree(graph):
    number_of_subtrees = [0 for _ in range(len(graph))]
    for i in range(len(graph)):
        if graph[i]:
            number_of_subtrees[i] = DFS(graph, i) - 1 # liczy samego siebie wiec trzeba go odjąć
    return number_of_subtrees


graph = [[] for _ in range(8)]
add_edge(0, 1, graph)
add_edge(0, 2, graph)
add_edge(1, 3, graph)
add_edge(1, 4, graph)
add_edge(1, 5, graph)
add_edge(2, 6, graph)
add_edge(2, 7, graph)
print(count_sub_tree(graph))
