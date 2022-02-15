
def relax(u, v, distance, parent):
    if distance[v] > distance[u] + G[u][v]:
        distance[v] = distance[u] + G[u][v]
        parent[v] = u


def bellman_Ford(graph, s):
    distance = [float('inf')] * len(graph)  #  dla każdego wierzchołka dystans wynosi inf tylko dla startowego zero
    parent = [None] * len(graph)
    distance[s] = 0

    # relaksacja
    for i in range(len(graph) - 1):  # kązdy obied ustala koszto dojścia do przynajmniej jednego wiezchołka dlatego musimy wykonac go dla n-1 wierzchołków, ponieważ wierzchołek starrtowy ma zero
        for u in range(len(graph)):   # dla każdej krawędzi wykonujemy relaksajce i powtarzamy to E -1  razy
            for v in range(len(graph)):
                if graph[u][v] != 0:
                    relax(u, v, distance, parent)

    # weryfikacja
    for u in range(len(graph)):   # sprawdzanie czy w grafie nie występuje ujemny cykl, przeglądamy jeszcze raz krawędzie
        for v in range(len(graph)): # i jesli natrafimy na krawedz której koszt dojscia jest wiekszy to mamy cykl ujemny
            if graph[u][v] != 0 and distance[v] > distance[u] + graph[u][v]:
                return False

    return distance, parent


if __name__ == '__main__':
    G = [[0, 2, 4, 0, 0],
         [0, 0, 3, 3, 0],
         [0, 0, 0, -1, 4],
         [0, 3, 0, 0, 2],
         [0, 0, 0, 0, 0]]
    print(bellman_Ford(G, 0))