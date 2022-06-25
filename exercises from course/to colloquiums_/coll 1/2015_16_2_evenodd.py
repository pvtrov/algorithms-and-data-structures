"""
Dana jest n elementowa tablica A zawierająca liczby naturalne (potencjalnie bardzo duże).
Wiadomo, że tablica A powstała w dwóch krokach. Najpierw wygenerowano losowo (z nieznanym
rozkładem) n różnych liczn nieparzystych i posortowano je rosnąco. Następnie wybrano losowo
dlog ne elementów powstałej tablicy i zamieniono je na losowo wybrane liczby parzyste. Proszę
zaproponować (bez implementacji!) algorytm sortowania tak powstałych danych. Algorytm
powinien być możliwie jak najszybszy. Proszę oszacować i podać jego złożoność czasową.
"""

"""
przechodzimy po tablicy, jak natrafiamy na parzysty element to zapamietujemy index, sprawdzamy czy pasuje do miejsca na 
ktorym sie znajduje jesli nie to robimy sprawdzamy czy trezba go przesunac w prawo czy w lewo i wykonujemy zmodyfikowany
partirion na tej czesci.
gdy element znajdzie sie na odpowiedniej pozycji to kontynuujemy przejscie od zapamietanego indeksu.
O(nlogn)
"""


def switch_to_right_place(array, index, side):
    moving_elem = array[index]
    if side == "left":
        while 0 <= index and array[index-1] > moving_elem:
            array[index-1], array[index] = array[index], array[index-1]
            index -= 1
    else:
        while index < len(array) and array[index+1] < moving_elem:
            array[index+1], array[index] = array[index], array[index+1]
            index += 1


def even_and_some_odd(array):
    for i in range(1, len(array)-1):
        if array[i]%2 == 0:
            if array[i] < array[i-1]:
                switch_to_right_place(array, i, "left")
            elif array[i] > array[i+1]:
                switch_to_right_place(array, i, "notleft")

    return array


array = [1, 3, 5, 2, 9, 11, 4, 13]
print(even_and_some_odd(array))