def DFS_stack(u, graph, visited, stack):
    visited[u] = True
    for v in range(len(graph[u])):
        if graph[u][v] != 0:
            if not visited[v]:
                DFS_stack(v, graph, visited, stack)
    stack.append(u)


def strongly_connected_component(graph):
    visited = [False for _ in range(len(graph[0]))]
    stack = []
    for v in range(len(graph[0])):
        if not visited[v]:
            DFS_stack(v, graph, visited, stack)
    new_graph = [[0 for _ in range(len(graph[0]))] for _ in range(len(graph[0]))]

    for i in range(len(graph[0])):
        for j in range(len(graph[0])):
                new_graph[j][i] = graph[i][j]

    visited = [False for _ in range(len(graph))]
    stack1 = []
    tab = []

    while stack:
        v = stack.pop()
        if not visited[v]:
            DFS_stack(v, new_graph, visited, stack1)
            tab.append(stack1)
            stack1 = []
    return tab


if __name__ == '__main__':
    # graph = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    #          [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    #          [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    #          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #          [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    #          [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    #          [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #          [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    #          [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    #          [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]]
    # graph = [[0, 1, 1, 0, 0, 0, 0],
    #          [0, 0, 0, 1, 0, 0, 1],
    #          [0, 1, 0, 0, 1, 0, 0],
    #          [0, 0, 1, 0, 0, 1, 0],
    #          [1, 0, 0, 0, 0, 1, 0],
    #          [1, 0, 0, 0, 0, 0, 1],
    #          [0, 0, 0, 1, 1, 0, 0]]
    graph = [[0, 1, 0, 0, 0, 0],
             [0, 0, 1, 0, 0, 1],
             [1, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 1, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 1, 0]]


    print(strongly_connected_component(graph))