from queue import Queue


def BFS(graph, start):
    queue = Queue()
    visited = [False for _ in range(len(graph[0]))]
    distance = [-1 for _ in range(len(graph[0]))]
    parent = [None for _ in range(len(graph[0]))]

    distance[start] = 0
    visited[start] =  True
    queue.put(start)

    while queue.qsize():
        u = queue.get()
        for i in range(len(graph[u])):
            if graph[u][i] != 0:
                if not visited[i]:
                    visited[i] = True
                    distance[i] = distance[u] + 1
                    parent[i] = u
                    queue.put(i)

    return visited, distance, parent


if __name__ == '__main__':
    graph = [[0, 0, 1, 0, 0, 1],
             [0, 0, 0, 1, 0, 1],
             [1, 0, 0, 1, 1, 0],
             [0, 1, 1, 0, 1, 0],
             [0, 0, 1, 1, 0, 1],
             [1, 1, 0, 0, 1, 0]]

    print(BFS(graph, 0))