"""
Zaproponuj algorytm, który policzy ile jest najkrótszych ścieżek w grafie z danego wierzchołka
u do v. Wskazówka: Dla każdej najkrótszej ścieżki przechodzącej przez wierzchołek w,
odległość w od startu jest taka sama jak odległość w do mety.
"""


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
        if all_paths[i] == end:
            paths[helper].append(all_paths[i])
            helper += 1
            continue
        else:
            paths[helper].append(all_paths[i])

    return paths


def number_of_shortest_paths(graph, start, end):
    all_paths = getting_result(graph, start, end)
    min_ = min(len(all_paths[i]) for i in range(len(all_paths)))

    result = 0
    for i in range(len(all_paths)):
        if len(all_paths[i]) == min_:
            result += 1

    return result


graph = [[2, 5, 3],
         [3, 5],
         [0, 4],
         [1, 0, 4],
         [2, 3, 5],
         [0, 1, 4]
         ]
print(number_of_shortest_paths(graph, 0, 4))