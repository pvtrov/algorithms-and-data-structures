# Proszę zaproponować algorytm scalający k posortowanych list.


def heapify(A, n, i):  # O(logn)
    l = 2 * i + 1  # lewy
    r = 2 * i + 2  # prawy
    m = i

    if l < n and A[l] > A[m]:
        m = l
    if r < n and A[r] > A[m]:
        m = r
    if m != i:
        A[i], A[m] = A[m], A[i]
        heapify(A, n, m)
    return A


def buildheap(A):  # O(nlogn)/O(n)
    n = len(A)
    for i in range(n // 2 - 1, -1, -1):
        heapify(A, n, i)
    return A


def heapsort(A):  # O(nlogn)
    n = len(A)
    buildheap(A)
    for i in range(n - 1, 0, -1):
        A[i], A[0] = A[0], A[i]
        heapify(A, i, 0)
    return A


def add_element(heap, v):  # kopiec, wartość elementu
    heap.append(v)
    n = len(heap)
    i = n - 1  # przypisuje indeks wstawionemu elementowi
    j = (i - 1) // 2  # indeks rodzica
    while i > 0 and heap[j] >= v:
        heap[i], heap[j] = heap[j], heap[i]
        i = j
        j = (i - 1) // 2
    return heap


def merging(first, second, third, fourth):
    arrays = [second, third, fourth]
    result = buildheap(first)
    for i in range(len(arrays)):
        for j in range(len(arrays[i])):
            result = add_element(result, arrays[i][j])
    print(result)
    return heapsort(result)


if __name__ == '__main__':
    first = [9, 2, 3, 4, 5, 6, 7, 8]
    second = [3, 3, 3, 6, 8, 9, 10]
    third = [2, 5, 8, 9]
    fourth = [1, 3, 4, 4, 4, 6, 7, 90]
    print(merging(first, second, third, fourth))
