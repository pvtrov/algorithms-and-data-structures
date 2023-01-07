def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]

    if start == end:
        return path

    if len(graph[start]) == 0:
        return None

    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest


graph = [[3, 4], [2, 3], [1, 4], [0, 1, 4], [0, 2, 3]]
print(find_shortest_path(graph, 0, 2, []))