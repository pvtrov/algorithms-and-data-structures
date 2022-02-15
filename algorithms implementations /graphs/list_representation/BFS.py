from queue import Queue


def BFS(graph, start):
    queue = Queue()
    visited = [False for _ in range(len(graph))]
    distance = [-1 for _ in range(len(graph))]
    parent = [None for _ in range(len(graph))]

    distance[start] = 0
    visited[start] = True
    queue.put(start)

    while queue.qsize():
        u = queue.get()
        for v in graph[u]:
            if not visited[v[0]]:
                visited[v[0]] = True
                distance[v[0]] = distance[u] + 1
                parent[v[0]] = u
                queue.put(v[0])

    print(visited)
    print(distance)
    print(parent)
    return visited, distance, parent


# graph = [[2, 5],
#          [3, 5],
#          [0, 3],
#          [1, 2, 4],
#          [2, 3, 5],
#          [0, 1, 4]
#          ]
graph = [[[2, 8]],
         [[2, 5]],
         [[0, 8], [1, 5], [3, 6]],
         [[2, 6], [4, 7], [5, 9]],
         [[3, 7]],
         [[3, 9], [6, 4], [7, 6]],
         [[5, 4]],
         [[5, 6]]]

BFS(graph, 0)
