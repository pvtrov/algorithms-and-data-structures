from queue import Queue


def topology_sort(graph):
    def DFS_visit(graph, u):
        nonlocal time
        time += 1
        visited[u] = True

        for each in range(len(graph[u])):
            if graph[u][each] != 0:
                if not visited[each]:
                    parent[each] = u
                    DFS_visit(graph, each)
        time += 1
        topologicly_sorted.insert(0, u)

    visited = [False for _ in range(len(graph[0]))]
    parent = [None for _ in range(len(graph[0]))]
    time = 0
    topologicly_sorted = []

    for each in range(len(graph[0])):
        if not visited[each]:
            DFS_visit(graph, each)

    return topologicly_sorted


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

    return distance


graph = [[0, 1, 1, 1, 0, 0],
         [0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0]]


def shortest_path_in_DAG(graph):
    TPsorted = topology_sort(graph)
    print(TPsorted)


print(shortest_path_in_DAG(graph))
