"""
Mamy daną tablicę stringów, gdzie suma długości wszystkich stringów daje n. Napisz algorytm, który posortuje tę tablicę
w czasie O(n). Można założyć, że stringi składają się wyłącznie z małych liter alfabetu łacińskiego.
"""


def radix_sort(array, n, d):
    for j in range(1, n):
        while j > 0:
            if array[j][d] < array[j-1][d]:
                array[j], array[j-1] = array[j-1], array[j]
            j -= 1
    return array


def sum_string(array):
    numbers_of_buckets = max(len(array[i]) for i in range(len(array)))
    buckets = [[] for _ in range(numbers_of_buckets+1)]
    for i in range(len(array)):
        buckets[len(array[i])].append(array[i])

    for i in range(numbers_of_buckets, 0, -1):
        if buckets[i]:
            C = radix_sort(buckets[i], len(buckets[i]), i-1)
            buckets[i - 1] = buckets[i] + buckets[i-1]
    return C


array = ["aga", "aba", "aaa", "agad", "kuba", "martyna", "agadaba"]
print(sum_string(array))