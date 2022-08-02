

def floydWarshall(G):
    result = []
    S = [[float('inf') for _ in range(len(G))] for _ in range(len(G))]
    for i in range(len(G)):  # Tablica dynamiczna z kosztami przejsc dla każdej pary wierzchołków
        for j in range(len(G)):
            if G[i][j] != 0:
                S[i][j] = G[i][j]
            if i == j:
                S[i][j] = 0

    for v in range(len(G)):
        for u in range(len(G)):
            for w in range(len(G)):
                S[u][w] = min(S[u][w], S[u][v] + S[v][w])  # jesli koszt z u, w jest mniejszy niż koszt
    for each in S:                                          # z u do v i z v do w to aktualizujemy tablice
        result.append(each)

    print(S)


G = [[0, 2, 4, 0, 0],
     [0, 0, 3, 3, 0],
     [0, 0, 0, -1, -2],
     [0, 3, 0, 0, 2],
     [0, 0, 0, 0, 0]]

floydWarshall(G)