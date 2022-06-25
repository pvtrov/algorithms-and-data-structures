from zad2testy import runtests
from math import inf

""" 
usuwam kazda z kraedzi i sprawdzam co sie dzieje
Dla kazdego wierzchołka sprawdzam czy jego sasiedzi sa liscmi, jesli tak to odzanaczam ze sprawdzone, jesli nie to
usuwam krawedz i zapisuje minimum, potem ide dalej itd (algorytm coś na stylu DFS)
złożonść chyba O(n^2) < dla kazdej krawedzi przechodze po kazdej krawedzi >
"""


class Node:
    def __init__(self):  # stwórz węzeł drzewa
        self.edges = []  # lista węzłów do których są krawędzie
        self.weights = []  # lista wag krawędzi
        self.ids = []  # lista identyfikatorów krawędzi
        self.is_checked = False  # czy juz sprawdzony

    def addEdge(self, x, w, id):  # dodaj krawędź z tego węzła do węzła x
        self.edges.append(x)  # o wadze w i identyfikatorze id
        self.weights.append(w)
        self.ids.append(id)


def is_leaf(vertex):
    if len(vertex.edges) > 0:
        return False
    else:
        return True


def checking_after_removing(vertex, removing_index, sum):
    for i in range(len(vertex.edges)):
        if vertex.ids[i] != removing_index:
            sum += vertex.weights[i]
            if not is_leaf(vertex.edges[i]):
                sum += checking_after_removing(vertex.edges[i], removing_index, sum)
    return sum


def tuturutu(T, min_sum, best_result):
    for neighbour in range(len(T.edges)):
        sum = 0
        if T.edges[neighbour].is_checked is False:
            first = checking_after_removing(T, T.ids[neighbour], sum)
            second = checking_after_removing(T.edges[neighbour], T.ids[neighbour], sum)
            difference = (first - second)
            if difference < min_sum:
                min_sum = difference
                best_result = T.ids[neighbour]
            tuturutu(T.edges[neighbour], min_sum, best_result)
    return best_result


def balance(Tk):
    min_sum = inf
    best_result = None

    best_result = tuturutu(Tk, min_sum, best_result)

    return best_result


runtests(balance)
