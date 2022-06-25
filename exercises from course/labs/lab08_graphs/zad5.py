# Dana jest mapa kraju w postaci grafu G = (V, E). Kierowca chce przejechać
# z miasta (wierzchołka) s to miasta t. Niestety niektóre drogi (krawędzie) są płatne. Każda droga ma taką
# samą jednostkową opłatę. Proszę podać algorytm, który znajduje trasę wymagającą jak najmniejszej liczby
# opłat. W ogólności graf G jest skierowany, ale można najpierw wskazać algorytm dla grafu nieskierowanego.


from math import inf


def cheapest_path(graph, start, end, path):
    path = path + [start]

    if start == end:
        return path

    if len(graph[start]) == 0:
        return None

    result = None
    min_sum = inf
    temp_sum = 0
    for node in graph[start]:
        if node[0] not in path:
            temp_sum = temp_sum + node[1]
            new_path = cheapest_path(graph, node[0], end, path)
            if new_path:
                if not result or temp_sum <= min_sum:
                    result = new_path
                    min_sum = temp_sum
    return result


if __name__ == '__main__':
    graph = [[(1, 0), (5, 1)],
             [(0, 0), (2, 1), (8, 0), (6, 1)],
             [(1, 1), (3, 1), (8, 1)],
             [(2, 1), (8, 0), (4, 1)],
             [(3, 1), (7, 0), (6, 0), (5, 0)],
             [(0, 1), (6, 0), (4, 0)],
             [(1, 1), (7, 1), (4, 0), (5, 0)],
             [(4, 0), (6, 1), (8, 1)],
             [(1, 0), (2, 1), (3, 0), (7, 0)]]
    path = []
    print(cheapest_path(graph, 3, 6, path))
