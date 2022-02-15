from queue import Queue


def shortestpath(graph, start, end):
    visited = [False for _ in range(len(graph[0]))]
    queue = Queue()
    path = [None for _ in range(len(graph[0]))]
    path[start] = -1
    paths = []
    queue.put(start)
    visited[start] = True

    while not queue.empty():
        v = queue.get()
        if v == end:
            while v != -1:
                paths.insert(0, v)
                v = path[v]
            return paths
        for u in range(len(graph[v])):
            if graph[v][u] != 0:
                if visited[u] is False:
                    path[u] = v
                    queue.put(u)
                    visited[u] = True


if __name__ == '__main__':
    graph = [[0, 0, 1, 1, 1],
             [0, 0, 0, 1, 0],
             [1, 0, 0, 1, 1],
             [1, 1, 1, 0, 1],
             [1, 0, 1, 1, 0]]

    print(shortestpath(graph, 0, 1))