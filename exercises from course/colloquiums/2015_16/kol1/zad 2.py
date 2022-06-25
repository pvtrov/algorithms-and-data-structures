"""Dana jest n elementowa tablica A zawierająca liczby naturalne (potencjalnie bardzo duże).
Wiadomo, że tablica A powstała w dwóch krokach. Najpierw wygenerowano losowo (z nieznanym
rozkładem) n różnych liczn nieparzystych i posortowano je rosnąco. Następnie wybrano losowo
dlog ne elementów powstałej tablicy i zamieniono je na losowo wybrane liczby parzyste. Proszę
zaproponować (bez implementacji!) algorytm sortowania tak powstałych danych. Algorytm
powinien być możliwie jak najszybszy. Proszę oszacować i podać jego złożoność czasową.
"""

""" przechodzimy po tablicy, jesli liczba jest nieparzysta to idziemy dalej, jeśli jest parzysta to przesuwamt
na odpowiednie miejsce, złożoność to O(n)
"""


def right(array, index):
    if array[index] > array[index + 1]:
        temporary = array[index]
        array[index] = array[index + 1]
        array[index + 1] = temporary
        index += 1
        right(array, index)
    return array


def left(array, index):
    if array[index] < array[index - 1]:
        temporary = array[index]
        array[index] = array[index - 1]
        array[index - 1] = temporary
        index -= 1
        left(array, index)
    return array


def move(array, index):
    if index == 0 or array[index] > array[index + 1]:
        right(array, index)

    if index == len(array) - 1 or array[index] < array[index - 1]:
        left(array, index)
    return array


def weird_sort(array):
    for i in range(len(array)):
        if array[i] % 2 == 0:
            move(array, i)

    return array


if __name__ == '__main__':
    array = [1, 7, 2, 4, 15, 6, 25]
    print(weird_sort(array))
