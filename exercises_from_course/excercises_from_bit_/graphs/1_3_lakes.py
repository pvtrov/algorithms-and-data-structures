"""
Dana jest dwuwymiarowa tablica N x N, w której każda komórka ma wartość “W” - reprezentującą wodę lub “L” - ląd.
Grupę komórek wody połączonych ze sobą brzegami nazywamy jeziorem.
a) Policz, ile jezior jest w tablicy
b) Policz, ile komórek zawiera największe jezioro
c) Zakładając, że pola o indeksach [0][0] i [n-1][n-1] są lądem, sprawdź czy da się przejść drogą lądową z pola [0][0]
do pola [n-1][n-1]. Można chodzić tylko na boki, nie na ukos.
d) Znajdź najkrótszą ścieżkę między tymi punktami. Wypisz po kolei indeksy pól w tej ścieżce
"""
from math import inf
from queue import Queue, PriorityQueue


def linear_index(row, column, n):
    return column + n * row


def cubic_index(index, n):
    return index // n, index % n


def is_valiable(row, col, n):
    return 0 <= row < n and 0 <= col < n


def DFS_a(G):
    def any_not_0(col):
        for i in range(len(G)):
            if G[col][i] != 0:
                return True
        return False

    def DFS_Visit(G, u, parent, visited):
        nonlocal time
        time += 1
        visited[u] = True
        for v in range(n):
            if G[u][v] != 0 and not visited[v]:
                parent[v] = u
                DFS_Visit(G, v, parent, visited)
        time += 1

    n = len(G)
    parent = [None] * n
    visited = [False] * n
    time = 0
    lakes_count = 0
    for u in range(n):
        if not visited[u]:
            DFS_Visit(G, u, parent, visited)
            if any_not_0(u):
                lakes_count += 1

    return lakes_count


def DFS_b(G):
    size = 0
    maximal_size = -1

    def any_not_0(col):
        for i in range(len(G)):
            if G[col][i] != 0:
                return True
        return False

    def DFS_Visit(G, u, parent, visited):
        nonlocal time
        nonlocal size
        time += 1
        size += 1
        visited[u] = True
        for v in range(n):
            if G[u][v] != 0 and not visited[v]:
                parent[v] = u
                DFS_Visit(G, v, parent, visited)
        time += 1

    n = len(G)
    parent = [None] * n
    visited = [False] * n
    time = 0
    for u in range(n):
        size = 0
        if not visited[u]:
            DFS_Visit(G, u, parent, visited)
            if size > maximal_size:
                maximal_size = size
    return maximal_size


def make_graph_c_d(matrix):
    n = len(matrix)
    options = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    graph = [[0 for _ in range(n**2)] for _ in range(n**2)]
    is_it_lake = [False for _ in range(n**2)]
    for column in range(n):
        for row in range(n):
            new_index = linear_index(row, column, n)
            if matrix[row][column] == 1:
                is_it_lake[new_index] = True
            for opt in options:
                tmp_cords = (row + opt[0], column + opt[1])
                if is_valiable(tmp_cords[0], tmp_cords[1], n):
                    graph[linear_index(row, column, n)][linear_index(tmp_cords[0], tmp_cords[1], n)] = 1
                    graph[linear_index(tmp_cords[0], tmp_cords[1], n)][linear_index(row, column, n)] = 1

    return graph, is_it_lake


def make_graph_a_b(matrix):
    n = len(matrix)
    options = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    graph = [[0 for _ in range(n ** 2)] for _ in range(n ** 2)]
    # is_it_lake = [None for _ in range(n ^ 2)]
    for column in range(n):
        for row in range(n):
            new_index = linear_index(row, column, n)
            for opt in options:
                tmp_cords = (row + opt[0], column + opt[1])
                if is_valiable(tmp_cords[0], tmp_cords[1], n) and matrix[row][column] == 1 and matrix[tmp_cords[0]][tmp_cords[1]] == 1:
                    # print(n, tmp_cords, linear_index(tmp_cords[0], tmp_cords[1], n))
                    graph[linear_index(row, column, n)][linear_index(tmp_cords[0], tmp_cords[1], n)] = 1
                    graph[linear_index(tmp_cords[0], tmp_cords[1], n)][linear_index(row, column, n)] = 1

    # tworzy pojedyncze jeziorka
    for i in range(n**2):
        c = cubic_index(i, n)
        if matrix[c[0]][c[1]] == 1:
            graph[i][i] = 1

    return graph


def BFS(graph, start, is_this_lake):
    queue = Queue()
    visited = [False for _ in range(len(graph[0]))]
    distance = [-1 for _ in range(len(graph[0]))]
    parent = [None for _ in range(len(graph[0]))]

    distance[start] = 0
    visited[start] = True
    queue.put(start)

    while queue.qsize():
        neighbour = queue.get()
        for i in range(len(graph[0])):
            if graph[neighbour][i] != 0 and is_this_lake[i] is False:
                if not visited[i]:
                    visited[i] = True
                    distance[i] = distance[neighbour] + 1
                    parent[i] = neighbour
                    queue.put(i)
    return visited


def print_path(parent, i, t):
    if parent[i] == -1:
        t.append(i)
        return t
    t = print_path(parent, parent[i], t)
    t.append(i)
    return t


def print_solution(distance, parent, s, destination):
    print(s, "to", destination, "is ", distance[destination])
    print(print_path(parent, parent[destination], []))


def dijkstra(graph, start, destination, is_this_lake):
    n = len(graph)
    distance = [inf for _ in range(n)]
    parent = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]
    visited[start] = True
    pq = PriorityQueue()
    distance[start] = 1

    for i in range(n):
        pq.put((distance[i], i))
    while not pq.empty():
        d, vertex = pq.get()
        if vertex == destination:
            return print_solution(distance, parent, start, destination)
        for u in range(n):
            if graph[vertex][u] != 0 and not visited[u] and not is_this_lake[u]:
                if distance[vertex] + graph[vertex][u] < distance[u]:
                    distance[u] = distance[vertex] + graph[vertex][u]
                    parent[u] = vertex
                    pq.put((distance[u], u))


def case_a(matrix):
    graph = make_graph_a_b(matrix)
    return DFS_a(graph)


def case_b(matrix):
    graph = make_graph_a_b(matrix)
    return DFS_b(graph)


def case_c(matrix):
    graph, lakes = make_graph_c_d(matrix)
    visited = BFS(graph, 0, lakes)
    return visited[-1]


def case_d(matrix):
    n = len(matrix)
    graph, lakes = make_graph_c_d(matrix)
    return dijkstra(graph, 0, linear_index(n-1, n-1, n), lakes)


# 0 - land
# 1 - lake

# 3, 2
M0 = [[0, 1, 1],
      [0, 0, 0],
      [1, 0, 0]]

# 2, 15
M1 = [
    [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
    [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
    [ 0,  0,  1,  1,  1,  1,  0,  0,  0,  0],
    [ 0,  0,  1,  1,  1,  1,  1,  0,  0,  0],
    [ 0,  0,  1,  1,  1,  0,  1,  0,  0,  0],
    [ 0,  0,  0,  0,  1,  1,  0,  0,  0,  0],
    [ 0,  1,  0,  0,  0,  0,  1,  1,  1,  1],
    [ 0,  1,  1,  1,  0,  0,  1,  0,  0,  0],
    [ 0,  1,  1,  1,  1,  0,  1,  0,  0,  0],
    [ 0,  0,  0,  0,  0,  0,  1,  0,  0,  0],
]

# 12, 9
M2 = [
    [ 0,  0,  0,  0,  0,  0,  1,  1,  0,  0],
    [ 0,  1,  1,  0,  0,  0,  1,  1,  0,  0],
    [ 1,  1,  1,  1,  0,  0,  0,  0,  1,  1],
    [ 0,  1,  1,  1,  0,  0,  0,  0,  1,  1],
    [ 1,  0,  0,  0,  0,  1,  1,  0,  0,  0],
    [ 0,  0,  0,  1,  0,  1,  1,  0,  1,  1],
    [ 1,  1,  0,  1,  0,  0,  0,  0,  1,  1],
    [ 1,  1,  0,  0,  0,  1,  1,  0,  0,  0],
    [ 0,  0,  1,  1,  0,  1,  1,  1,  0,  0],
    [ 1,  0,  1,  1,  0,  0,  0,  0,  1,  0],
]

# 10, 7,
M3 = [
    [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
    [ 0,  1,  0,  1,  0,  0,  1,  0,  1,  0],
    [ 0,  0,  0,  1,  0,  0,  1,  0,  0,  0],
    [ 0,  1,  0,  1,  0,  0,  1,  0,  1,  0],
    [ 0,  0,  0,  1,  0,  0,  1,  0,  0,  0],
    [ 0,  1,  0,  1,  0,  0,  1,  0,  1,  0],
    [ 0,  0,  0,  1,  0,  0,  1,  0,  0,  0],
    [ 0,  1,  0,  1,  0,  0,  1,  0,  1,  0],
    [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
    [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
]

# print(case_a(M3))
# print(case_b(M0))
# case_b(M0)
# print(case_c(M1))
case_d(M0)