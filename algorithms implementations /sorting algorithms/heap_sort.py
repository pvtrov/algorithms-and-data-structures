
def heapify(A, n, i):  # O(logn)
    l = 2 * i +1  # lewy
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


def wkladanie_el_do_kopca(heap, v):  # kopiec, wartość elementu
    heap.append(v)
    n = len(heap)
    i = n - 1  # przypisuje indeks wstawionemu elementowi
    j = (i - 1) // 2  # indeks rodzica
    while i > 0 and heap[j] <= v:
        heap[i], heap[j] = heap[j], heap[i]
        i = j
        j = (i - 1) // 2
    return heap


A = [0, 8, 5, 3, 8, 5, 1]
heap = buildheap(A)
result = wkladanie_el_do_kopca(heap, 7)
print(heapsort(result))