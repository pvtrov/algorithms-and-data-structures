"""Cyfra jednokrotna to taka, która występuje w danej liczbie dokładnie
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
""" najpierw zliczam ile jakich cyfr maja poszczegolne liczby i zapisuje to do tablicy, potem sortuje, najwpierw
wedlug jednowymiarowych, potem dwuwymiarowych, na koniec odpowiednie liczby wpisuje do końcowej tablicy, dzieki indexom
które zawarłam w result_array, O(n) :)
"""


def counting(result_array, count_array, index):
    for i in range(10):
        if count_array[i] == 1:
            result_array[index][0] += 1
        if count_array[i] > 1:
            result_array[index][1] += 1
    return result_array


def count(array, result_array):  # O(10n) ( w tym counting)
    for i in range(len(array)):
        result_array[i][2] += i
        count_array = [0] * 10
        while array[i] > 0:
            count_array[(array[i] % 10)] += 1
            array[i] = array[i] // 10
        result_array = counting(result_array, count_array, i)
    return result_array


def bubbleSort_one(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j][0] < arr[j + 1][0]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def sort_two(array):
    for i in range(len(array)-1):
        if array[i][0] == array[i + 1][0]:
            if array[i][1] > array[i + 1][1]:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
    return array


def pretty_sort(array):
    to_solve = array.copy()
    result_array = [[0, 0, 0] for _ in range(len(array))]  # jednokrotne, wielokrotne, index liczby w wejsciowej tab
    result_array = count(array, result_array)
    # teraz jeszcze musze posortowac, robie bombelkiem bo moge
    almost_sorted = bubbleSort_one(result_array)
    sorted = sort_two(almost_sorted)
    final_array = []
    for i in range(len(sorted)):
        final_array.append(to_solve[sorted[i][2]])

    return final_array


if __name__ == '__main__':
    array = [123, 455, 2344, 1266, 114577, 67333]
    print(pretty_sort(array))
