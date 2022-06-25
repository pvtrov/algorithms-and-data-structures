# Proszę zaimplementować algorytm QuickSort bez użycia rekurencji (ale można wykorzystać
# własny stos).


def partition(T, p, r):
    x = T[r]
    i = p - 1
    for j in range(p, r):
        if T[j] <= x:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i + 1], T[r] = T[r], T[i + 1]
    return i + 1


def quick(T):
    tab = [(0, len(T)-1)]
    while len(tab):
        left, right = tab.pop()
        if left < right:
            q = partition(T, left, right)
            tab.append((q+1, right))
            tab.append((left, q-1))
    return T

if __name__ == '__main__':
    tab = [9, 6, 2, 7, 9, 1, 0, 6, 3, 2, 5, 7]
    print(quick(tab))