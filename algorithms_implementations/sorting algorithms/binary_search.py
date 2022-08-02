
def binary_search(left, right, array, element):
    middle = left + right // 2
    if array[middle] == element:
        return middle
    elif array[middle] < element:
        binary_search(middle, right, array, element)
    else:
        binary_search(right, middle, array, element)


array = [1, 2, 4, 6, 8, 9, 12, 23, 45, 46]
print(binary_search(0, len(array)-1, array, 8))