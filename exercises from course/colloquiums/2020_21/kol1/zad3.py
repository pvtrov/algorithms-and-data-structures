from zad3testy import runtests

from math import inf


def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        variable = bucket[i]
        j = i - 1
        while j >= 0 and variable < bucket[j]:
            bucket[j + 1] = bucket[j]
            j = j - 1
        bucket[j + 1] = variable


def SortTab(T, P):
    minimum = inf
    maximum = -inf

    for i in range(len(P)):
        if P[i]:
            if P[i][0] < minimum:
                minimum = P[i][0]
            if P[i][1] > maximum:
                maximum = P[i][1]

    number_of_ranges = maximum - minimum // 2

    buckets = [[] for _ in range(number_of_ranges)]

    for number in T:
        buckets[int(number - minimum)].append(number)

    result = []
    for i in range(len(buckets)):
        if buckets[i]:
            insertion_sort(buckets[i])  # 7,48s 7/10

        result.extend(buckets[i])

    return result

runtests( SortTab )
