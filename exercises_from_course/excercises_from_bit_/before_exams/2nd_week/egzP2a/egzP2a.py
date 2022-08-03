import copy

# pomysl git tylko jebie sie implementacja
# mozna wprowadzic troche poprawek

from egzP2atesty import runtests


def partition(A, right, left):
    x = A[left][1]
    i = right-1
    for j in range(right, left):
        if A[j][1] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[left] = A[left], A[i+1]
    return i+1


def select(A, right, left, index):
    if right == left:
        return A[index]
    q = partition(A, right, left)
    if q == index:
        return A[q]
    elif index < q:
        return select(A, right, q-1, index)
    else:
        return select(A, q+1, left, index)


def zdjecie(T, m, k):
    items = [[0 for _ in range(3)] for _ in range(m)]
    start = 0
    end = k - 1

    for i in range(m):
        A = copy.deepcopy(T)
        start_item = select(A, 0, len(A)-1, start)
        end_item = select(A, 0, len(A)-1, end)
        items[i][0] = start_item
        items[i][1] = end_item
        items[i][2] = m - i - 1
        start = end + 1
        end = start + k

    for elem in A:
        for i in range(len(items)):
            if items[i][0][1] <= elem[1] < items[i][1][1] or elem[1] == items[i][1][1]:
                if items[i][2] < len(T):
                    T[items[i][2]] = elem
                    items[i][2] += k
                    break
    return T


# m = 2 #Ilość rzędów
# k = 2 #Ilość osób w najniższym rzędzie
# T = [ (1001, 154),(1002, 176),(1003, 189),(1004, 165),(1005, 162) ]
# print(zdjecie(T, m, k))

runtests ( zdjecie, all_tests=False )