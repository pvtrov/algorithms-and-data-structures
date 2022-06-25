"""
Dana jest tablica 2n liczb rzeczywistych. Zaproponuj algorytm, który podzieli te liczby na n par w taki sposób, że
podział będzie miał najmniejszą maksymalną sumę liczb w parze. Przykładowo, dla liczb (1, 3, 5, 9) możemy mieć podziały
((1,3),(5,9)), ((1,5),(3,9)), oraz ((1,9),(3,5)). Sumy par dla tych podziałów to (4, 14), (6, 12) oraz (10, 8), w
związku z tym maksymalne sumy to 14, 12 oraz 10. Wynika z tego, że ostatni podział ma najmniejszą maksymalną sumę.
"""


def partition(array, p, r):
    pivot = array[r]
    i = p-1

    for j in range(p, r):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[r] = array[r], array[i+1]
    return i+1


def quicksort(array, p, r):
    if p < r:
        q = partition(array, p, r)
        quicksort(array, p, q-1)
        quicksort(array, q+1, r)


def divide_by_sum(array):
    quicksort(array, 0, len(array)-1)
    result = [[] for _ in range(len(array)//2)]
    length = len(array)
    for i in range(length//2):
        result[i] = [array[i], array[length-1-i]]

    return result


# array = [1, 3, 5, 9]
array = [5, 7, 8, 3, 2, 4]
print(divide_by_sum(array))