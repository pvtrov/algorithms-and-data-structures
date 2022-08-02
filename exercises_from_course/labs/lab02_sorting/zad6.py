# Dany jest ciąg przedziałów domkniętych [a1, b1], . . . ,[an, bn]. Proszę
# zapropnować algorytm, który znajduje taki przedział [at, bt], w którym w całości zawiera się jak najwięcej
# innych przedziałów.

def bubble_sort(array):
    length_of_array = len(array)
    for i in range(length_of_array - 1):
        for j in range(0, length_of_array - i - 1):
            if array[j][0] > array[j + 1][0]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def ranges(sorted_array):
    result = ()
    max_number = 0
    for i in range(len(sorted_array)):
        counter = 0
        for j in range(i, len(sorted_array)):
            if array[i][1] > array[j][1]:
                counter += 1
                if counter > max_number:
                    max_number = counter
                    result = array[i]
    return result


if __name__ == '__main__':
    array = [(2, 6), (4, 8), (3, 5), (7, 11), (2, 8), (4, 7), (1, 3), (8, 11)]
    sorted_array = bubble_sort(array)
    print(ranges(sorted_array))
