"""
Dany jest graf G = (V, E), którego wierzchołki reprezentują punkty
nawigacyjne nad Bajtocją, a krawędzie reprezentują korytarze powietrzne między tymi punktami. Każdy
korytarz powietrzny ei ∈ E powiązany jest z optymalnym pułapem przelotu pi ∈ N (wyrażonym w metrach).
Przepisy dopuszczają przelot danym korytarzem jeśli pułap samolotu różni się od optymalnego najwyżej o t
metrów. Proszę zaproponować algorytm (bez implementacji), który sprawdza czy istnieje możliwość przelotu
z zadanego punktu x ∈ V do zadanego punktu y ∈ V w taki sposób, żeby samolot nigdy nie zmieniał pułapu.
Algorytm powinien być poprawny i możliwie jak najszybszy. Proszę oszacować jego złożoność czasową.
"""

""" musimy znaleźć sciezke któa spełnia zalozenia, jesli taka jest istnieje zwracamy True, jeśli nie to
zwracamy False"""


def find_right_path(graph, start, end, path, t, airplane):
    path = path + [start]

    if start == end:
        return path

    if len(graph[start]) == 0:
        return None

    new_path = None
    for vertex in graph[start]:
        if vertex[1] - t < airplane < vertex[1] + t:
            if vertex[0] not in path:
                new_path = find_right_path(graph, vertex[0], end, path, t, airplane)
    return new_path


def safe_fly(graph, start, end, t, airplane):
    path = find_right_path(graph, start, end, [], t, airplane)
    if path is None or len(path) <= 1:
        return False
    else:
        return True


graph = [[(1, 6), (2, 7), (4, 5)],
         [(0, 6), (4, 6)],
         [(0, 7), (3, 4), (4, 9)],
         [(2, 4), (4, 5)],
         [(3, 5), (2, 9), (1, 6), (0, 5)]]

print(safe_fly(graph, 4, 3, 2, 8))
