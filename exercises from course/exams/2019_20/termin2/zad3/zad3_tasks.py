from zad3testy import runtests

"""
Dany jest zbiór N zadań, gdzie niektóre zadania muszą być wykonane przed innymi zadaniami.
Wzajemne kolejności zadań opisuje dwuwymiarowa tablica T[N][N]. Jeżeli T[a][b] = 1 to wykonanie zadania a musi 
poprzedzać wykonanie zadania b. W przypadku gdy T[a][b] = 2 zadanie b musi być wykonane wcześniej, 
a gdy T[a][b] = 0 kolejność zadań a i b jest obojętna. Proszę zaimplementować funkcję tasks(T), 
która dla danej tablicy T, zwraca tablicę z kolejnymi numerami zadań do wykonania.

Przykład Dla tablicy T = [ [0,2,1,1], [1,0,1,1], [2,2,0,1], [2,2,2,0] ] wynikiem
jest tablica [1,0,2,3]
"""

""" 
budujemy graf skierowany i robimy sortowanie topologiczne  
złożoność czasowa jak i pamieciowa to O(n^2)
"""


def dfs_rec(graph, start, path, visited):
    visited[start] = True
    for edge in range(len(graph[0])):
        if graph[start][edge] != 0:
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


def make_graph(graph, task):
    for i in range(len(task)):
        for j in range(len(task)):
            if task[i][j] == 1:
                graph[i][j] = 1
            elif task[i][j] == 2:
                graph[j][i] = 1
            else:
                continue
    return graph


def tasks(T):
    graph = [[0 for _ in range(len(T))] for _ in range(len(T))]
    make_graph(graph, T)
    result = DFS(graph)
    return result





runtests( tasks )
