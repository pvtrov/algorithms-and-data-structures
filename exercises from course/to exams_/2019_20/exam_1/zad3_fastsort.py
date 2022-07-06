from zad3testy import runtests
import math
"""
Pewien eksperyment fizyczny daje w wyniku liczby rzeczywiste postaci a^x, gdzie a to pewna stała większa od 1 (a > 1) 
zaś x to liczby rzeczywiste rozłożone równomiernie na przedziale [0, 1].
Napisz funkcję fast sort, która przyjmuje tablicę liczb z wynikami eksperymentu oraz stałą a i
zwraca tablicę z wynikami eksperymentu posortowanymi rosnąco. Funkcja powinna działać możliwie jak najszybciej. 
Uzasadnij poprawność zaproponowanego rozwiązania i oszacuj jego złożoność obliczeniową. 
"""


def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        variable = bucket[i]
        j = i - 1
        while j >= 0 and variable < bucket[j]:
            bucket[j + 1] = bucket[j]
            j = j - 1
        bucket[j + 1] = variable


def bucket_sort(array):  # O(n)
    max_value = max(array)
    size = max_value / len(array)

    buckets_list = []
    for x in range(len(array)):
        buckets_list.append([])

    for i in range(len(array)):
        j = int(array[i] / size)
        if j != len(array):
            buckets_list[j].append(array[i])
        else:
            buckets_list[len(array) - 1].append(array[i])

    for s in range(len(array)):
        insertion_sort(buckets_list[s])

    final_array = []
    for x in range(len(array)):
        final_array = final_array + buckets_list[x]
    return final_array


def fast_sort(tab, a):
    for i in range(len(tab)):   # O(n)
        tab[i] = math.log(tab[i], a)

    tab = bucket_sort(tab)
    for i in range(len(tab)):
        tab[i] = a**tab[i]

    return tab



runtests( fast_sort )
