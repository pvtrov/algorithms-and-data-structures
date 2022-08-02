"""
Dana jest nieskończona tablica A, gdzie pierwsze n pozycji zawiera posortowane liczby naturalne, a reszta tablicy ma
wartości None. Nie jest dana wartość n. Przedstaw algorytm, który dla danej liczby naturalnej x znajdzie indeks w
tablicy, pod którym znajduje się wartość x. Jeżeli nie ma jej w tablicy, to należy zwrócić None.
"""


def binary_search(array, start, end, element):
    middle = (start + end) // 2
    if start == end:
        if array[start] == element:
            return start
        else:
            return None

    if array[middle] == element:
        return middle
    elif array[middle] > element:
        return binary_search(array, start, middle-1, element)
    else:
        return binary_search(array, middle+1, end, element)


def find_x(array, x):
    n = 1

    while array[n] is not None and array[n] < x:
        n *= 2

    result = binary_search(array, 0, n, x)
    return result


array = [1, 2, 3,4, 5, 6, 7, 8, None, None, None ,None ,None,  None, None, None ,None ,None, None, None, None ,None ,None, None, None, None ,None ,None]
print(find_x(array, 10))