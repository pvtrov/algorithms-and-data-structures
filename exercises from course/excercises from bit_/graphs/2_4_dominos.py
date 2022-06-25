"""
Mamy pewien układ klocków domino. Otrzymujemy go w postaci listy par [a, b]: Jeżeli przewrócimy klocek a, to klocek b
też się przewróci. Chcemy znaleźć minimalną liczbę klocków, które trzeba przewrócić ręcznie, aby wszystkie domina były
przewrócone.
"""
"""
buduje graf, puszczam sobie dfs, i w klockach przewróconych przesz inne klocki zazanzczam w tablicy jako True 
<ze przewrócone przez inne>, pote zliczam ile nie zostalo przewroconych przez inne i to jest moja minimalna liczba
"""


def DFS_visit(G, u, visited, parent, flipped):
    visited[u] = True
    for v in G[u]:
        if not visited[v]:
            flipped[v] = True
            parent[v] = u
            DFS_visit(G, v, visited, parent, flipped)


def DFS(G):
    visited = [False for _ in range(len(G))]
    flipped = [False for _ in range(len(G))]
    parent = [-1 for _ in range(len(G))]
    for u in range(len(G)):
        if not visited[u]:
            DFS_visit(G, u, visited, parent, flipped)
    return flipped


def make_graph(dominos):
    max_size = -1
    for i in range(len(dominos)):
        if max_size < dominos[i][0]:
            max_size = dominos[i][0]
        elif max_size < dominos[i][1]:
            max_size = dominos[i][1]

    new_graph = [[] for _ in range(max_size+2)]
    for i in range(len(dominos)):
        new_graph[dominos[i][0]].append(dominos[i][1])

    return new_graph


def count_flips(dominos):
    graph = make_graph(dominos)
    flipped = DFS(graph)
    counter = 0

    for i in range(len(flipped)):
        if flipped[i] is not True:
            counter += 1

    return counter


dominos = [[2, 3], [3, 5], [6, 7], [7, 8], [8, 10], [11, 13], [14, 15], [9, 12], [2, 4], [3, 9]]
dominos1 = [[2, 3], [3, 5], [6, 7], [7, 8], [8, 10], [11, 13], [14, 15]]
print(count_flips(dominos1))