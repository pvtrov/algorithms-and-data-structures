# Dana jest tablica A zawierająca n parami różnych liczb. Proszę zaproponować algorytm, który
# znajduje takie dwie liczby x i y z A, że y −x jest jak największa oraz w tablicy nie ma żadnej liczby z takiej,
# że x < y < z (innymi słowy, po posortowaniu tablicy A rosnąco wynikiem byłyby liczby A[i] oraz A[i+1] dla
# których A[i + 1] − A[i] jest największe).


def partition(T, p, r):
    x = T[r]
    i = p - 1
    for j in range(p, r):
        if T[j] <= x:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i + 1], T[r] = T[r], T[i + 1]
    return i + 1


def select(A, p, r, k):  # statystyki pozycyjne
    if p == r:
        return A[p]
    q = partition(A, p, r)
    if q == k:
        return A[q]
    elif k < q:
        return select(A, p, q - 1, k)
    else:
        return select(A, q + 1, r, k)

def difference(A):
    x = select(A, 0, len(A)-1, len(A)-1)
    y = select(A, 0, len(A)-1, len(A)-2)
    print(x, y)

if __name__ == '__main__':
    A = [9, 6, 4, 7, 2, 7, 5, 1, 2, 10]
    difference(A)