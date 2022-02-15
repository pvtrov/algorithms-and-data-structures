

def cycle(graph):
    queue = []
    visited = [False for _ in range(len(graph))]
    parents = [None for _ in range(len(graph))]
    visited[0] = True
    queue.append(0)

    while queue:
        s = queue.pop(0)
        for v in graph[s]:
            if parents[s] != v and v != s:
                if visited[v] is False:
                    queue.append(v)
                    visited[v] = True
                    parents[v] = s
                else:
                    return True
    return False


if __name__ == '__main__':
    graph = [[1, 2], [0, 2, 3], [0, 1], [1]]

    print(cycle(graph))