from queue import Queue

def cycle(G):
    Q = []
    visited = [False for _ in range(len(G))]
    prev = [None for _ in range(len(G))]
    visited[0] = True
    Q.append(0)

    while Q:
        s = Q.pop(0)
        for v in G[s]:
            if prev[s] != v and v != s:
                if visited[v] == False:
                    Q.append(v)
                    visited[v] = True
                    prev[v] = s
                else:
                    return True
    return False

#################################################

def neighbours(G, s):
    neighbour = []
    for i in range(len(G[s])):
        if G[s][i] == 1:
            neighbour.append(i)
    return neighbour

def cycle(graf):
    queue = []
    color = [None] * len(graf)
    prev = [None] * len(graf)
    color[0] = True
    queue.append(0)

    while queue:
        s = queue.pop(0)
        for v in neighbours(graf,s):
            if prev[s] != v and v != s:
                if color[v] == None:
                    queue.append(v)
                    color[v] = True
                    prev[v] = s
                else:
                    return True
    return False

if __name__ == '__main__':
    graph = [[0, 1, 1, 0],
             [1, 0, 1, 1],
             [1, 1, 0, 0],
             [0, 1, 0, 0]]
    print(cycle(graph))