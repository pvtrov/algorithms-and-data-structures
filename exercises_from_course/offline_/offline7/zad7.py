from zad7testy import runtests

# pólnocna -> True
# południowa -> False


class Vertex:
    def __init__(self):
        self.index = None


def DFS(u, graph, deleted, cycle, vertex_counter):
    for v in graph[u]:      # przechodze po sasiadach
        if deleted[u][v] is False:      # jesli nie krawedz jest nie usunieta to ja usuwam
            deleted[u][v] = True
            deleted[v][u] = True
            cycle = DFS(v, graph, deleted, cycle, vertex_counter)
            cycle.append(u)
            if u not in vertex_counter:
                vertex_counter.append(u)
    return cycle


def euler(graph):
    for i in range(len(graph)):  # sprawdzam czy moze byc cykl
        if len(graph[i]) == 0 or len(graph[i]) % 2 != 0:
            return None

    deleted = [[False for _ in range(len(graph))] for _ in range(len(graph))] # macierz usunietych krawedzi
    cycle = [0]             # odpoweidnie wierzchołki cyklu
    vertex_counter = []         # użyte wierzchołki, pomoze w stwerdzeniu czy graf jest spojny
    cycle = DFS(0, graph, deleted, cycle, vertex_counter)
    if len(vertex_counter) != len(graph):   # jeśli liczba wierzchołkow w cyklu jest inna od liczby wierzchlkow w grafie
        return None                         # oznacza ze graf jest niespojny
    return cycle


def give_me_graph(list):
    graph = [[] for _ in range(2*len(list))]

    for i in range(len(list)):
        for j in range(2):
            if j == 0:
                graph[2*i] = list[i][j]
                for k in range(len(graph[2*i])):
                    graph[2*i][k] = 2*graph[2*i][k]
            if j == 1:
                graph[2*i+1] = list[i][j]
                for k in range(len(graph[2*i+1])):
                    graph[2*i+1][k] = 2*graph[2*i+1][k]
        graph[2*i].append(2*i+1)
        graph[2*i+1].append(2*i)

    return graph


def give_me_right_output(cycle):
    road = []

    for i in range(len(cycle)-1):
        if cycle[i] == cycle[i+1] + 1 and cycle[i+1] % 2 == 0:
            road.append(cycle[i+1]//2)
        elif cycle[i] == cycle[i+1] - 1 and cycle[i] % 2 == 0:
            road.append(cycle[i]//2)



    return road


def droga( G ):
    graph = give_me_graph(G)
    cycle = euler(graph)
    road = give_me_right_output(cycle)
    return road

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( droga, all_tests = True )
# G = [ ([1],[2,3,4]),
#       ([0],[2,5,6]),
#       ([1,5,6],[0,3,4]),
#       ([0,2,4],[5,7,8]),
#       ([0,2,3],[6,7,9]),
#       ([1,2,6],[3,7,8]),
#       ([1,2,5],[4,7,9]),
#       ([4,6,9],[3,5,8]),
#       ([3,5,7],[9]),
#       ([4,6,7],[8]) ]
# print(droga(G))
