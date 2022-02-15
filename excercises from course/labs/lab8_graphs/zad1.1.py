# 1. Sprawdzanie czy graf jest dwudzielny (czyli zauważyć, że to 2-kolorowanie i użyć DFS lub BFS).


def if_bipartite(graph, start):
    visited = [False for _ in range(len(graph))]
    red = [False for _ in range(len(graph))]
    blue = [False for _ in range(len(graph))]
    red[start] = True
    visited[start] = True
    for vertex in range(len(graph)):
        for i in range(len(graph[vertex])):
            neighbour = graph[vertex][i]
            if not visited[neighbour]:
                visited[neighbour] = True
                if red[vertex]:
                    blue[neighbour] = True
                else:
                    red[neighbour] = True
            else:
                if red[neighbour] and red[vertex] or blue[neighbour] and blue[vertex]:
                    return "nie"
    return "tak"

if __name__ == '__main__':
    graph = [[1, 2, 4],
             [0, 2, 3],
             [0, 1, 3],
             [1, 2, 4],
             [3, 0]]
    print(if_bipartite(graph, 0))