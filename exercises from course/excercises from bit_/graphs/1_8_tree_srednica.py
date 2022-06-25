"""
Średnicą drzewa nazywamy odległość między jego najbardziej oddalonymi od siebie wierzchołkami.
Napisz algorytm, który przyjmując na wejściu drzewo (niekoniecznie binarne!) w postaci listy krawędzi zwróci jego średnicę.
"""


def add_edge(parent, child, graph):
    graph[parent].append(child)


def dfs_counter(graph, vertex, counter, visited, max_counter):
    visited[vertex] = True
    counter += 1
    for i in graph[vertex]:
        if not visited[i]:
            if counter >= max_counter:
                max_counter = counter
                x = i
            max_counter = dfs_counter(graph, i, counter, visited, max_counter)
    return max_counter


def DFS(graph, vertex, max_counter):
    visited = [False for _ in range(len(graph))]
    parent = [-1 for _ in range(len(graph))]
    counter = 0

    return dfs_counter(graph, vertex, counter, visited, max_counter)


def tree_srednica(graph):
    max_values = [0 for _ in range(len(graph))]

    for i in range(len(graph)):
        max_values[i] = DFS(graph, i, -1)
    return max(max_values)


graph = [[] for _ in range(8)]
add_edge(0, 1, graph)
add_edge(1, 0, graph)
add_edge(2, 0, graph)
add_edge(0, 2, graph)
add_edge(3, 1, graph)
add_edge(1, 3, graph)
add_edge(4, 1, graph)
add_edge(1, 4, graph)
add_edge(5, 1, graph)
add_edge(1, 5, graph)
add_edge(6, 2, graph)
add_edge(2, 6, graph)
add_edge(7, 2, graph)
add_edge(2, 7, graph)
print(tree_srednica(graph))
