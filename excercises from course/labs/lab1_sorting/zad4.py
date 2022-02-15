# Proszę zaimplementować funkcję, która mając na wejściu tablicę n elementów
# oblicza jednocześnie jej największy i najmniejszy element wykonując 1.5n porównań.

from math import inf


def find_minimum(array):
    temporary_minimum = True
    minimum = inf
    for index in range(0, len(array)-1, +2):
        if array[index] >= array[index+1]:
            temporary_minimum = array[index+1]
        else:
            temporary_minimum = array[index]

        if temporary_minimum < minimum:
            minimum = temporary_minimum

    if minimum > array[len(array)-1]:
        minimum = array[len(array)-1]

    return minimum


def find_maximum(array):
    temporary_maximum = True
    maximum = -inf
    for index in range(0, len(array) - 1, +2):
        if array[index] <= array[index + 1]:
            temporary_maximum = array[index + 1]
        else:
            temporary_maximum = array[index]

        if temporary_maximum > maximum:
            maximum = temporary_maximum

    if maximum < array[len(array) - 1]:
        maximum = array[len(array) - 1]

    return maximum


def finding(array):         #O(n)
    minimum = find_minimum(array)
    maximum = find_maximum(array)

    return minimum, maximum

if __name__ == '__main__':
    #array = [1, 9, 5, 6, 12, 3, 0, -3, 19]
    #array = [-1, -3, -100, 67, 109, 4567, 0]
    #array = [0, 656, 34, -90, 89, -90]
    print(finding(array))

