# Znany operator telefonii komórkowej Pause postanowił zakonczyc działalnosc w
# Polsce. Jednym z głównych elementów całej procedury jest wyłaczenie wszystkich stacji nadawczych (które
# tworza spójny graf połaczen). Ze wzgledów technologicznych urzadzenia nalezy wyłaczac pojedynczo a operatorowi
# dodatkowo zalezy na tym, by podczas całego procesu wszyscy abonenci znajdujacy sie w zasiegu
# działajacych stacji mogli sie ze soba łaczyc (czyli by graf pozostał spójny). Proszę zaproponować algorytm
# podający kolejność wyłączania stacji.

def remove_edges(graph, vertex):
    length = len(graph[vertex])
    for i in range(len(graph[vertex])):
        graph[graph[vertex][i]].remove(vertex)

    for i in range(length):
        del graph[vertex][0]

    return graph


def pause(graph, vertex, removed, result, parent):
    helper = 0
    vertex_length = len(graph[vertex])
    if not removed[vertex]:
        neighbour = 0
        for i in range(len(graph[vertex])):
            if graph[vertex][neighbour] != parent and len(graph[graph[vertex][neighbour]]) > 2:
                helper += 1
                neighbour += 1

            elif graph[vertex][neighbour] != parent and len(graph[graph[vertex][neighbour]]) == 2:
                result, removed, graph = pause(graph, graph[vertex][neighbour], removed, result, vertex)
                helper += 1
                neighbour += 1

            elif len(graph[graph[vertex][neighbour]]) == 1:
                removed[graph[vertex][neighbour]] = True
                result.append(graph[vertex][neighbour])
                remove_edges(graph, graph[vertex][neighbour])

        if helper == len(graph[vertex]):
            removed[vertex] = True
            result.append(vertex)
            remove_edges(graph, vertex)

    return result, removed, graph


if __name__ == '__main__':
    # graph = [[1, 4, 6],
    #          [0, 2, 7],
    #          [1, 3, 7],
    #          [2, 4, 6],
    #          [0, 3, 5, 7],
    #          [4, 6],
    #          [0, 3, 5],
    #          [1, 2, 4]
    #          ]
    graph = [[1, 2, 4, 5],
             [0, 3, 5],
             [0, 4, 6],
             [1],
             [0, 2],
             [0, 1, 6],
             [2, 5]]

    removed = [False for _ in range(len(graph))]
    result = []
    for vertex in range(len(graph)):
        result, removed, graph = pause(graph, vertex, removed, result, -1)

    print(result)
