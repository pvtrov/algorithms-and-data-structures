def DFSstack(u, G, visited, stack):
    visited[u] = True
    for v in G[u]:
        if not visited[v]:
            DFSstack(v, G, visited, stack)
    stack.append(u)


def strongly_connected_component(G):
    visited = [False for _ in range(len(G))]
    stack = []
    for v in range(len(G)):  # dfs dla grafu wyjsciowego, zapisując czasy ich przetworzenia
        if not visited[v]:
            DFSstack(v, G, visited, stack)
    # transponowanie grafu
    Gt = [[] for _ in range(len(G))]  # odwaracanie krawedzi grafu
    for i in range(len(G)):
        for j in G[i]:
            Gt[j].append(i)
    visited = [False for _ in range(len(G))]
    stack1 = []
    tab = []
    while stack:  # dfs drugi raz w odwróconej koeljności
        v = stack.pop()
        if not visited[v]:
            DFSstack(v, Gt, visited, stack1)
            tab.append(stack1)
            stack1 = []
    return tab


if __name__ == '__main__':
    # G = [[1], [0, 2], [1]]

    # G = [[1], [2], [0, 6, 4], [2], [3], [2], [5, 7], [8], [6]]
    # G = [[1], [2, 4], [3, 7], [0], [5], [6], [4], [8], [9], [7]]
    G =  [[], [0, 9], [], [2, 10], [], [], [], [], [7, 9], [1, 8, 6, 5], [3, 4]]
    print(strongly_connected_component(G))
