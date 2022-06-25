# Proszę zaimplementować funkcję wstawiającą dowolny element do kopca binarnego

def add_element(heap, v):  # kopiec, wartość elementu
    heap.append(v)
    n = len(heap)
    i = n - 1  # przypisuje indeks wstawionemu elementowi
    j = (i - 1) // 2  # indeks rodzica
    while i > 0 and heap[j] <= v:
        heap[i], heap[j] = heap[j], heap[i]
        i = j
        j = (i - 1) // 2
    return heap

heap = [10, 8, 6, 1]
print(add_element(heap, 7))