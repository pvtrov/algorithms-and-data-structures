# Wierzchołek v w grafie skierowanym nazywamy dobrym początkiem jeśli
# każdy inny wierzchołek można osiągnąć scieżką skierowaną wychodzącą z v. Proszę podać algorytm, który
# stwierdza czy dany graf zawiera dobry początek


def good_start(graph):
    for vertex in range(len(graph)):
        if len(graph[vertex]) == len(graph)-1:
            return vertex
        else:
            continue
    return "brak"

if __name__ == '__main__':
    graph = [[1, 2, 3, 4], [2, 4], [3], [], []]
    print(good_start(graph))