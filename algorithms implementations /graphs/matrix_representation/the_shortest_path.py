def find_shortest_path(graph, start, end, path):
    path = path + [start]

    if start == end:
        return path

    shortest = None
    for vertex in range(len(graph[start])):
        if graph[start][vertex] != 0:
            if vertex not in path:
                new_path = find_shortest_path(graph, vertex, end, path)
                if new_path:
                    if not shortest or len(new_path) < len(shortest):
                        shortest = new_path
    return shortest


graph = [[0, 0, 0, 1, 1],
         [0, 0, 1, 1, 0],
         [0, 1, 0, 0, 1],
         [1, 1, 0, 0, 1],
         [1, 0, 1, 1, 0]]

print(find_shortest_path(graph, 0, 2, []))