"""
Cyfra jednokrotna to taka, która występuje w danej liczbie dokładnie
jeden raz. Cyfra wielokrotna to taka, która w liczbie występuje więcej niż jeden raz. Mówimy,
że liczba naturalna A jest ładniejsza od liczby naturalnej B jeżeli w liczbie A występuje więcej
cyfr jednokrotnych niż w B, a jeżeli cyfr jednokrotnych jest tyle samo to ładniejsza jest ta
liczba, która posiada mniej cyfr wielokrotnych. Na przykład: liczba 123 jest ładniejsza od
455, liczba 1266 jest ładniejsza od 114577, a liczby 2344 i 67333 są jednakowo ładne.
Dana jest tablica T zawierająca liczby naturalne. Proszę zaimplementować funkcję:
pretty_sort(T)
która sortuje elementy tablicy T od najładniejszych do najmniej ładnych. Użyty algorytm
powinien być możliwie jak najszybszy. Proszę w rozwiązaniu umieścić 1-2 zdaniowy opis
algorytmu oraz proszę oszacować jego złożoność czasową.
"""


def partition(array, p, r):
    pivot = array[r][0]
    i = p-1
    for j in range(p, r):
        if array[j][0] <= pivot:
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


def sort_whole(array):
    i = 0
    while i+1 < len(array):
        while i+1 < len(array) and array[i][0] == array[i+1][0]:
            if array[i][1] < array[i+1][1]:
                array[i], array[i+1] = array[i+1], array[i]
                i += 1
            else:
                i += 1
        i += 1
    return array


def count_numbers(array, index, result):
    counters = [0] * 10
    number = array[index]

    while number != 0:
        c = number % 10
        counters[c] += 1
        number = number//10

    one_digit, more_digit = 0, 0
    for i in range(10):
        if counters[i] == 1:
            one_digit += 1
        elif counters[i] > 1:
            more_digit += 1

    return one_digit, more_digit, index


def pretty_sort(array):
    n = len(array)
    result = [[0, 0, 0] for _ in range(n)] # cj, cw, index

    for i in range(n):
        result[i] = count_numbers(array, i, result)

    result = quicksort(result, 0, n-1)
    result = sort_whole(result)

    final_list = []
    for i in range(n-1, -1, -1):
        final_list.append(array[result[i][2]])
    return final_list


# array = [123, 455, 1266, 114775, 2344, 67333]
array = [5415, 6565, 8838, 4475, 3939, 9753, 2423, 9034]
print(pretty_sort(array))