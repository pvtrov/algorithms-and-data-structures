def find_all_paths(graph, start, end, path):
    path = path + [start]
    if start == end:
        return path

    paths = []
    for vertex in range(len(graph[start])):
        if graph[start][vertex] != 0:
            if vertex not in path:
                new_paths = find_all_paths(graph, vertex, end, path)
                for new_path in new_paths:
                    paths.append(new_path)

    return paths


def getting_result(graph, start, end):
    all_paths = find_all_paths(graph, start, end, [])
    counter = 0
    for i in range(len(all_paths)):
        if all_paths[i] == end:
            counter += 1    # liczba sciezek

    paths = [[] for _ in range(counter)]
    helper = 0
    for i in range(len(all_paths)):
        if all_paths[i] == 2:
            paths[helper].append(all_paths[i])
            helper += 1
            continue
        else:
            paths[helper].append(all_paths[i])

    return paths


graph = [[0, 0, 0, 1, 1],
         [0, 0, 1, 1, 0],
         [0, 1, 0, 0, 1],
         [1, 1, 0, 0, 1],
         [1, 0, 1, 1, 0]]

print(getting_result(graph, 0, 2))