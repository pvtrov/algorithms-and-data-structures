# Mamy daną tablicę A z n liczbami. Proszę zaproponować algorytm o złożoności
# O(n), który stwierdza, czy istnieje liczba x (tzw. lider A), która występuje w A na ponad połowie pozycji.
from math import inf


def max_value(array):
    max = array[0]
    for i in range(len(array)):
        if array[i] > max:
            max = array[i]

    return max


def if_array_lider(array):
    counting_array = [0] * (max_value(array) + 1)
    for i in range(len(array)):
        counting_array[array[i]] += 1
        if counting_array[array[i]] > len(array) / 2:
            return "Yes"
    return "No"


if __name__ == '__main__':
    array = [-4, 5, 8, 3, 3, 3, 3, 3, 7]
    print(if_array_lider(array))
