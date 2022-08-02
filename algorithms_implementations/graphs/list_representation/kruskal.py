
class Node:
    def __init__(self, value):
        self.val = value
        self.rank = 0
        self.parent = self


def find(x):
    if x != x.parent:
        x.parent = find(x.parent)
    return x.parent


def union(x, y):
    x = find(x)
    y = find(y)

    if x == y: return

    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


def remove_edge(graph, u, v):
    graph[graph[u][v][0]].remove((u, graph[u][v][1]))


def kruskal(graph):
    length = len(graph)
    edges = []
    to_sort_edges = []
    for i in range(length):
        for j in range(len(graph[i])):
            to_sort_edges.append((graph[i][j][1], i, graph[i][j][0]))
            remove_edge(graph, i, j)  # usuwam juz wpisana krawedz żeby sie nie powtrorzyly
    to_sort_edges.sort(key=lambda to_sort_edges: to_sort_edges[0])

    for i in range(length):
        edges.append(Node(i))

    min_spanning_tree = []
    weight = 0
    for edge in range(length):
        v = edges[to_sort_edges[edge][1]]
        u = edges[to_sort_edges[edge][2]]
        if not find(v) is find(u):
            union(v, u)
            min_spanning_tree.append((v.val, u.val))
            weight += to_sort_edges[edge][0]

    return weight, min_spanning_tree


if __name__ == '__main__':
    graph = [[(1, 2), (2, 7), (3, 8), (5, 3)],
             [(0, 2), (4, 5)],
             [(0, 7), (3, 1)],
             [(2, 1), (0, 8), (5, 12), (4, 4)],
             [(3, 4), (1, 5), (5, 6)],
             [(0, 3), (3, 12), (4, 6)]]

    print(kruskal(graph))