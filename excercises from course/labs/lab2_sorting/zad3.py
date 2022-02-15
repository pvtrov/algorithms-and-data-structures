# Dana jest posortowana tablica A[1...n] oraz liczba x.
# Proszę napisać program, który stwierdza czy istnieją indeksy i oraz j takie, że A[i] + A[j] = x


def suming(array, x):  # o(n^2)
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i] + array[j] == x and i != j:
                return i, j

    return "brak indeksów"


if __name__ == '__main__':
    # array = [1, 3, 5, 9, 10, 12]
    array = [1, 3, 3, 7, 9]
    print(suming(array, 14))
