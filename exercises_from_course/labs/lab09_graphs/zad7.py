from math import inf
"""
Pewien podróżnik chce przebyć trasę z punktu A
do punktu B. Niestety jego samochód spala dokładnie jeden litr paliwa na jeden kilometr trasy. W baku mieści
się dokładnie D litrów paliwa. Trasa jest reprezentowana jako graf, gdzie wierzchołki to miasta a krawędzie to
łączące je drogi. Każda krawędź ma długość w kilometrach (przedstawioną jako licza naturalna). W każdym
wierzchołku jest stacja benzynowa, z daną ceną za litr paliwa. Proszę podać algorytm znajdujący trasę z
punktu A do punktu B o najmniejszym koszcie. Proszę uzasadnić poprawność algorytmu.
"""

"""
1. znajduje wszystkie sciezki którymi da sie dojechac do celu ( ich długość nie jest wieksza od pojemnosci baku samochodu)
2. sprawdzam któa jest najtansza zadając sobie pytania:
    * czy na tym co mam w baku dojade do celu?
        * Tak: gdzie cena jest niższa i czy mam miejsce w baku?
                * tu :  tankuje
                *tam : jade dalej
        * Nie: gdzie cena jest niższa?
                * tu: tankuje do pełna
                * tam : tankuje tak by dojechac
    """


def find_all_paths(graph, start, end, path, capacity):
    path = path + [start]
    if start == end:
        return path

    paths = []
    for vertex in range(len(graph[start])):
        if capacity > graph[start][vertex] > 0:
            if vertex not in path:
                new_paths = find_all_paths(graph, vertex, end, path, capacity)
                for new_path in new_paths:
                    paths.append(new_path)

    return paths


def getting_result(graph, start, end, capacity):
    all_paths = find_all_paths(graph, start, end, [], capacity)
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


def counting(path, capacity, actual_capacity, prices):
    cost = 0
    for station in range(len(path)-1):
        if actual_capacity < path[station+1]-path[station]:     # czy dojade do celu na aktualnym baku ?
            if prices[station] < prices[station+1]:             # gdzie nizsza cena ?
                tanked = capacity - actual_capacity
                actual_capacity = capacity
                cost += tanked * prices[station]
            else:
                tanked = (path[station+1]-path[station]) - actual_capacity
                actual_capacity = path[station+1]-path[station]
                cost += tanked * prices[station]
        else:
            if actual_capacity < capacity:
                if prices[station] < prices[station+1]:
                    tanked = capacity - actual_capacity
                    actual_capacity = capacity
                    cost += tanked * prices[station]
                else:
                    continue

    return cost, path


def tank(graph, start, purpose, prices, capacity):
    paths = getting_result(graph, start, purpose, capacity)
    min_cost = inf
    for i in range(len(paths)):
        actual_capacity = 0
        cost, path = counting(paths[i], capacity, actual_capacity, prices)
        if min_cost > cost:
            min_cost = cost

    return cost, path


graph = [[0, 0, 0, 5, 10],
         [0, 0, 3, 8, 0],
         [0, 3, 0, 0, 4],
         [5, 8, 0, 0, 7],
         [10, 0, 4, 7, 0]]
prices = [3, 4, 2, 5, 3]
print(tank(graph, 0, 2, prices, 9))