

def knap_sack(array_of_weights, array_of_things, max_weight):       #O(n*max_weight)
    array_of_weights_size = len(array_of_weights)

    result_array = [[0] * (max_weight + 1) for i in range(array_of_weights_size)]

    for w in range(array_of_weights[0], max_weight + 1):
        result_array[0][w] = array_of_things[0]

    for i in range(1, array_of_weights_size):
        for w in range(1, max_weight + 1):
            result_array[i][w] = result_array[i - 1][w]
            if w >= array_of_weights[i]:
                result_array[i][w] = max(result_array[i][w], result_array[i - 1][w - array_of_weights[i] + array_of_things[i]])

    return result_array[array_of_weights_size - 1][max_weight], result_array


def get_solution(result_array, array_of_weights, array_of_things, i, w):        #zwraca indeksy przedmiotw
    if i < 0:
        return []

    if i == 0:
        if w >= array_of_weights[0]:
            return 0
        return []

    if w >= array_of_weights[i] and result_array[i][w] == result_array[i-1][w-array_of_weights[i]+array_of_things[i]]:
        return get_solution(result_array, array_of_weights, array_of_things, i-1, w - array_of_weights[i]) + i

    return get_solution(result_array, array_of_weights, array_of_things, i-1, w)

