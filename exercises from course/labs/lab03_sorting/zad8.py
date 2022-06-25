# Proszę zaimplementować funkcję partition z algorytmu QuickSort
# według pomysłu Hoare’a (tj. mamy dwa indeksy, i oraz j, wędrujące z obu końców tablicy w stronę środka
# i zamieniamy elementy tablicy pod nimi jeśli mniejszy indeks wskazuje na wartość większą od piwota, a
# większy na mniejszą

def partitionH(T, left, right):
    pivot = T[left]
    i = left + 1
    j = right
    while True:
        while T[i] < pivot:
            if i == right:
                break
            i += 1

        while T[j] > pivot:
            j -= 1

        if i >= j:
            break
        #     return j

        T[i], T[j] = T[j], T[i]
        # i+=1
        # j-=1
    T[left], T[j] = T[j], T[left]
    return j

def quicksort(T, p, r):
    if p < r:
        q = partitionH(T, p, r)
        quicksort(T, p, q - 1)
        quicksort(T, q + 1, r)
    return T

if __name__ == '__main__':
    T = [9, 3, 5, 1, 3, 7, 5, 9, 0, 1, 4, 6]
    print(quicksort(T, 0, len(T)-1))