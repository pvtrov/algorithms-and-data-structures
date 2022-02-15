# Ścieżka Hamiltona to ścieżka przechodząca przez wszystkie
# wierzchołki w grafie, przez każdy dokładnie raz. W ogólnym grafie znalezienie ścieżki Hamiltona jest problemem
# NP-trudnym. Proszę podać algorytm, który stwierdzi czy istnieje ścieżka Hamiltona w acyklicznym grafie skierowanym.

def dfs_rec(graph, start, path, visited):
    visited[start] = True
    for edge in graph[start]:
        if edge not in path:
            # print(edge, path)
            dfs_rec(graph, edge, path, visited)
    path.insert(0, start)


def DFS(G):
    path = []
    visited = [False for _ in range(len(G))]
    for u in range(len(G)):
        if not visited[u]:
            dfs_rec(G, u, path, visited)
    return path


def if_hamilton_path(graph):
    sorted_path = DFS(graph)
    for v in range(len(sorted_path)-1):
        if sorted_path[v+1] in graph[sorted_path[v]]:
            continue
        else:
            return "nie"

    return sorted_path


if __name__ == '__main__':
    graph = [[6], [7, 2], [3], [7, 4], [5, 7], [7, 6], [], [0]]
    # graph = [[1, 2, 6], [], [3, 1], [4, 5], [], [], [3]]
    print(if_hamilton_path(graph))