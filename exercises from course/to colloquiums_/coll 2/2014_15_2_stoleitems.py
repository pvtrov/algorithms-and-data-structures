"""
Problem plecakowy - dwuwymiarowa wersja problemu - oprócz ciężaru jest wysokość towarów.

{p1, ..., pn} - przedmioty v(pi) - wartość przedmiotu pi
r(pi) - ciężar przedmiotu pi h(pi) - wysokość przedmiotu pi

Jaka jest największa możliwa sumaryczna wartość przedmiotów, których ciężar
nie przekracza M a wysokość S? Oszacować złożoność i udowodnić poprawność algorytmu.
(Nie trzeba implementować).
"""

"""
f(i, w, h) - najwiekszy zysk jaki mozna zyskac wybierajac do przedmiotu do i, nie przekraczajac wagi W i wysokosci H

f(0, w, h) = 0, w[0] > w lub/i h[0] > 0
           = P[0], w[0] <= w, h[0] < h
           
f(i, 0, h) lub f(i, 0, 0) lub f(i, w, 0) = 0

f(i, w, h) = max( f(i-1, w), f(i-1, w - W[i], h - H[i]) + P[i] )

"""


def knap_sack(array_of_weights, array_of_things, max_weight, array_of_heights, max_height):       #O(n*max_weight)
    array_of_weights_size = len(array_of_weights)

    result_array = [[[0] * (max_weight + 1) for _ in range(array_of_weights_size)] for _ in range(len(array_of_heights))]

    for w in range(array_of_weights[0], max_weight + 1):
        for h in range(array_of_heights[0], max_height + 1):
            result_array[0][w][h] = array_of_things[0]

    for i in range(1, array_of_weights_size):
        for w in range(1, max_weight + 1):
            for h in range(1, max_height + 1):
                result_array[i][w] = result_array[i - 1][w]
                if w >= array_of_weights[i] and h >= array_of_heights[i]:
                    result_array[i][w] = max(result_array[i][w][h],
                                             result_array[i - 1][w - array_of_weights[i]][h - array_of_heights[i]] + array_of_things[i])

    return result_array[array_of_weights_size - 1][max_weight][max_height], result_array


def get_solution(result_array, array_of_weights, array_of_things, array_of_heights, i, w, h):        #zwraca indeksy przedmiotw
    if i < 0:
        return []

    if i == 0:
        if w >= array_of_weights[0]:
            return 0
        return []

    if w >= array_of_weights[i] and result_array[i][w][h] == \
            result_array[i-1][w-array_of_weights[i]][h - array_of_heights[i]] + array_of_things[i]:
        return get_solution(result_array, array_of_weights, array_of_things, array_of_heights, i-1, w - array_of_weights[i], h - array_of_heights[i]) + i

    return get_solution(result_array, array_of_weights, array_of_things, array_of_heights, i-1, w, h)
