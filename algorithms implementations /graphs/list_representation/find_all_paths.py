def find_all_paths(graph, start, end, path):
    path = path + [start]
    if start == end:
        return path

    if len(graph[start]) == 0:
        return None

    paths = []
    for neighbour in graph[start]:
        if neighbour not in path:
            new_paths = find_all_paths(graph, neighbour, end, path)
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


graph = [[3, 4], [2, 3], [1, 4], [0, 1, 4], [0, 2, 3]]
print(getting_result(graph, 0, 2))