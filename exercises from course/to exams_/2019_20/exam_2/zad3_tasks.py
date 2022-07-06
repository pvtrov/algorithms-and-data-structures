from zad3testy import runtests
"""
Dany jest zbiór N zadań, gdzie niektóre zadania muszą być wykonane przed innymi zadaniami.
Wzajemne kolejności zadań opisuje dwuwymiarowa tablica T[N][N]. Jeżeli T[a][b] = 1 to wykonanie zadania a musi 
poprzedzać wykonanie zadania b. W przypadku gdy T[a][b] = 2 zadanie b musi być wykonane wcześniej, 
a gdy T[a][b] = 0 kolejność zadań a i b jest obojętna. Proszę zaimplementować funkcję tasks(T), która dla danej 
tablicy T, zwraca tablicę z kolejnymi numerami zadań do wykonania.
"""


def dfs_rec(graph, start, path, visited):
    visited[start] = True
    for edge in range(len(graph[0])):
        if graph[start][edge] == 1 and not visited[edge]:
            if edge not in path:
                dfs_rec(graph, edge, path, visited)
    path.insert(0, start)


def DFS(graph):
    path = []
    visited = [False for _ in range(len(graph[0]))]
    for u in range(len(graph[0])):
        if not visited[u]:
            dfs_rec(graph, u, path, visited)
    return path


def create_graph(T):
    n = len(T)
    for i in range(n):
        for j in range(n):
            if i == j:
                T[i][j] = -1
            elif T[i][j] == 1:
                T[j][i] = -1
            elif T[i][j] == 2:
                T[i][j] = -1
                T[j][i] = 1
            elif T[i][j] == 0:
                T[i][j] = 1
                T[j][i] = -1
    return T


def tasks(T):
    graph = create_graph(T)

    queueue = DFS(graph)
    return queueue


runtests( tasks )
