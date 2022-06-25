# Proszę zaimplementować funkcję, która otrzymuje na wejściu posortowaną niemalejąco tablicę A o rozmiarze n oraz liczbę
# x i sprawdza, czy x występuje w A. Jeśli tak, to zwraca najmniejszy indeks, pod którym x występuje.

def if_in_list(array, x):       #o(n)
    for i in range(len(array)):
        if array[i] == x:
            return i

    return "brak x w danej tablicy"


if __name__ == '__main__':
    #array = [2, 5, 6, 7, 7, 8, 9]
    #x = 7
    array = [0, 1, 2, 2, 2, 5, 7, 8, 90]
    x = 2
    print(if_in_list(array, x))