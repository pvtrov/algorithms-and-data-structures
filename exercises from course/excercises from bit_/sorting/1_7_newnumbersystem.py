"""
Dana jest tablica zawierająca n liczb z zakresu [0...n^2 -1]. Napisz algorytm, który posortuje taką tablicę w czasie O(n).
"""

"""
przyjmuje n jako podstawe systemu liczbowego
"""


def countsort(array, n, index):
    count = [0] * (n+1)
    output = [0] * len(array)

    for i in range(len(array)):
        count[array[i][index]] += 1

    for i in range(1, n+1):
        count[i] += count[i-1]

    i = n-1
    while i >= 0:
        output[count[array[i][index]] - 1] = array[i]
        count[array[i][index]] -= 1
        i -= 1

    for k in range(len(array)):
        array[k] = output[k]


def new_number_system(array, n):
    lenght = len(array)
    new_array_list = [0] * lenght
    result = [0] * lenght

    for i in range(lenght):
        new_array_list[i] = [array[i]//n, array[i] % n, i]

    for i in range(1, -1, -1):
        countsort(new_array_list, n, i)

    for i in range(lenght):
        result[i] = array[new_array_list[i][2]]

    return result


array = [7, 3, 8, 14]
print(new_number_system(array, 4))