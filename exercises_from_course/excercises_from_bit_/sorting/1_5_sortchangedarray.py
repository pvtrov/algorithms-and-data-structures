"""
Masz daną tablicę zawierającą n (n >= 11) liczb naturalnych w zakresie [0, k]. Zamieniono 10 liczb z tej tablicy na
losowe liczby spoza tego zakresu (np. dużo większe lub ujemne). Napisz algorytm, który posortuje tablicę w czasie O(n).
"""


def partition(array, p, r):
    pivot = array[r]
    i = p-1

    for j in range(p, r):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[r] = array[r], array[i+1]
    return i+1


def quicksort(array, p, r):
    if p < r:
        q = partition(array, p, r)
        quicksort(array, p, q-1)
        quicksort(array, q+1, r)
    return array


def countsort(array, k):
    counters = [0] * (k+1)
    result = [0] * len(array)
    for i in range(len(array)):
        counters[array[i]] += 1

    for i in range(1, len(counters)):
        counters[i] += counters[i-1]

    for k in range(len(array)-1, -1, -1):
        counters[array[k]] -= 1
        result[counters[array[k]]] = array[k]

    return result


def sort_changed_array(array, k):
    lesser = []
    bigger = []
    to_k = [0] * (len(array)-10)

    index = 0
    for i in range(len(array)):
        if array[i] < 0:
            lesser.append(array[i])
        elif array[i] > k:
            bigger.append(array[i])
        else:
            to_k[index] = array[i]
            index += 1

    lesser = quicksort(lesser, 0, len(lesser)-1)
    bigger = quicksort(bigger, 0, len(bigger)-1)
    to_k_ = countsort(to_k, k)

    lesser.extend(to_k_)
    lesser.extend(bigger)

    return lesser


array = [1, 2, -30, 4, -5, 3455, 1, 2, -4, 2, 478, 4, 6785, 1, 2, 323, 45, 3, -2, 4, 5, 1, 2, 3, -5, 4, 5]
print(sort_changed_array(array, 5))