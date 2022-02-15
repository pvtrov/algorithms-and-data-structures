# Proszę zaproponować i zaimplementować algorytm, który mając na wejściu tablicę A zwraca
# liczbę jej inwersji (t.j., liczbę par indeksów i < j takich, że A[i] > A[j].

def inversion(array):
    counter = 0
    for index in range(len(array) - 1):
        if array[index] > array[index + 1]:
            counter += 1

    return counter


if __name__ == '__main__':
    # array = [5, 2, 8, 9]
    array = [8, 2, 3, 4, 5, 1, 3, 4, 3]
    print(inversion(array))
