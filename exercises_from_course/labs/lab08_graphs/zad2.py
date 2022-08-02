# Mówimy, że wierzchołek t w grafie skierowanym jest uniwersalnym
# ujściem, jeśli
# (a) z każdego innego wierzchołka v istnieje krawędź z v do t
# (b) nie istnieje żadna krawędź wychodząca z t.

def universal_output(graph):
    length = len(graph)
    for i in range(length):
        counter = 0
        counter_nd = 0
        for j in range(length):
            counter += graph[i][j]
            counter_nd += graph[j][i]
        if counter == length-1 and counter_nd == 0 or counter == 0 and counter_nd == length-1:
            return i
    return "nie"

if __name__ == '__main__':
    graph = [[0, 0, 1, 0, 1, 1],
             [1, 0, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 1, 0, 1, 0],
             [0, 0, 1, 0, 0, 1],
             [0, 0, 1, 0, 0, 0]]
    print(universal_output(graph))