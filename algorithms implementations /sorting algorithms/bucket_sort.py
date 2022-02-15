# Sortowanie kubełkowe

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
