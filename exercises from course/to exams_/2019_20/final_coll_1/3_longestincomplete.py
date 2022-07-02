"""
Dana jest tablica A zawierająca n = len(A) liczb naturalnych. Dodatkowo wiadomo, że A w sumie
zawiera k różnych liczb (należy założyć, że k jest dużo mniejsze niż n). Proszę zaimplementować
funkcję longest incomplete(A, k), która zwraca długość najdłuższego spójnego ciągu elementów
z tablicy A, w którym nie występuje wszystkie k liczb. (Można założyć, że podana wartość k jest
zawsze prawidłowa.)
Przykład Dla tablicy
A = [1,100, 5, 100, 1, 5, 1, 5]
wartością wywołania longest incomplete(A, 3) powinno być 4 (ciąg 1, 5, 1, 5 z końca tablicy).
"""


def move_indexes(A, index, k, indexes):
    numbers = [A[index]]
    counter = 1
    i = index - 1

    while counter < k-1:
        if A[i] not in numbers:
            numbers.append(A[i])
            counter += 1
        i -= 1
    return i


def count_down_numbers(A, index, last_index, indexes):
    for i in range(index, last_index-1, -1):
        elem = A[i]
        val = indexes[elem]
        indexes[elem] = val - 1
    return indexes


def delete_numbers(indexes, unique):
    for elem in indexes:
        if indexes[elem] == 0:
            unique.remove(elem)

    return unique


def longest_incomplete(A, k):
    indexes = {}
    uniq_numbers = []
    lengths = [0] * len(A)
    lengths[0] = 1
    indexes[A[0]] = 1
    uniq_numbers.append(A[0])
    last_index = 0

    for i in range(1, len(A)):
        element = A[i]
        if element not in uniq_numbers:
            uniq_numbers.append(element)
            indexes[element] = 1
            if len(uniq_numbers) == k:
                index = move_indexes(A, i, k, indexes)
                indexes = count_down_numbers(A, index, last_index, indexes)
                last_index = index + 1
                length = i - index
                lengths[i] = length
                uniq_numbers = delete_numbers(indexes, uniq_numbers)
            else:
                lengths[i] = lengths[i-1] + 1
        else:
            lengths[i] = lengths[i - 1] + 1
            value = indexes[element]
            indexes[element] = value + 1

    return max(lengths)


A = [1, 100, 5, 100, 1, 5, 1, 5]
A1 = [6, 7, 8, 6, 5, 4, 3, 2, 6, 7, 8]
print(longest_incomplete(A1, 7))