# Dana jest tablica A zawierająca n elementów, z których każdy ma jeden z k kolorów.
# Proszę podać możliwie jak najszybszy algorytm, który znajduje indeksy i oraz j takie, że wsród elementów
# A[i], A[i + 1], . . . , A[j] występują wszystkie k kolorów oraz wartość j − i jest minimalna (innymi słowy,
# szukamy najkrótszego przedziału z wszystkimi kolorami).
from math import inf


def looking(array, k):
    if len(array) < k:
        return None

    min_length = inf
    for i in range(len(array)):
        counter = k
        counting_array = []
        length = 0
        for j in range(i, len(array)):
            if counter > 0:
                if array[j] not in counting_array:
                    counter -= 1
                    length += 1
                    counting_array.append(array[j])
                else:
                    length += 1
            else:
                if min_length > length:
                    min_length = length
                    result = (i, j - 1)
                    break
                else:
                    continue
    return result


if __name__ == '__main__':
    # array = [1, 2, 6, 2, 3, 2, 4, 5, 6, 1, 5, 4, 3]
    # k = 6
    array = [1, 2, 3, 1, 3, 2, 4, 1, 2]
    k = 4
    print(looking(array, k))
