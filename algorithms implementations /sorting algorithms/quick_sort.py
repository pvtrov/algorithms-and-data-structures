from random import randint
from statistics import median


# Zwykły quicksort
def partition(T, p, r):
    x = T[r]
    i = p - 1
    for j in range(p, r):
        if T[j] <= x:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i + 1], T[r] = T[r], T[i + 1]
    return i + 1


def quicksort(T, p, r):
    if p < r:
        q = partition(T, p, r)
        quicksort(T, p, q - 1)
        quicksort(T, q + 1, r)


# Quicksort z randomizacją

def randomized_partition(T, p, r):
    i = randint(p, r)
    T[r], T[i] = T[i], T[r]
    return partition(T, p, r)


def randomized_quicksort(T, p, r):
    if p < r:
        q = randomized_partition(T, p, r)
        randomized_quicksort(T, p, q - 1)
        randomized_quicksort(T, q + 1, r)


# Quicksort z medianą

def median_partition(T, p, r):
    a = randint(p, r)
    b = randint(p, r)
    x = median([T[r], T[a], T[b]])

    if x == T[a]:
        T[r], T[a] = T[a], T[r]
    elif x == T[b]:
        T[r], T[b] = T[b], T[r]

    return partition(T, p, r)


def median_quicksort(T, p, r):
    if p < r:
        q = median_partition(T, p, r)
        median_quicksort(T, p, q - 1)
        median_quicksort(T, q + 1, r)


# Quicksort bez rekursji ogonowej
def no_tail_quicksort(T, p, r):
    while p < r:
        q = partition(T, p, r)

        if (q - p) < (r - q):
            no_tail_quicksort(T, p, q - 1)
            p = q + 1
        else:
            no_tail_quicksort(T, q + 1, r)
            r = q - 1


# quicksort na linkedlisty
class Node:
    def __init__(self):
        self.value = None
        self.next = None


def printlist(L):
    while L is not None:
        print(L.value, "->", end=" ")
        L = L.next
    print("|")


def tab2list(A):
    H = Node()
    C = H
    for i in range(len(A)):
        X = Node()
        X.value = A[i]
        C.next = X
        C = X
    return H.next


def glue(lower, equal, higher):
    temporary_lower = lower
    while lower is not None and temporary_lower.next is not None:
        temporary_lower = temporary_lower.next
    temporary_equal = equal
    while equal is not None and temporary_equal.next is not None:
        temporary_equal = temporary_equal.next
    if lower is not None:
        temporary_lower.next = equal
        temporary_equal.next = higher
        return lower
    else:
        temporary_equal.next = higher
        return equal


def quickersort(array):
    if array is None:
        return array
    lower_array_to_sort = Node()
    higher_array_to_sort = Node()
    equal_before_sort = Node()
    sorted_lower_array = lower_array_to_sort
    sorted_higher_array = higher_array_to_sort
    equal_array = equal_before_sort
    pivot = array.value
    while array is not None:
        if array.value < pivot:
            sorted_lower_array.next = array
            sorted_lower_array = sorted_lower_array.next
            equal_array.next = array.next
            sorted_higher_array.next = array.next
        elif array.value == pivot:
            equal_array.next = array
            equal_array = equal_array.next
            sorted_higher_array.next = array.next
            sorted_lower_array.next = array.next
        else:
            sorted_higher_array.next = array
            sorted_higher_array = sorted_higher_array.next
            equal_array.next = array.next
            sorted_lower_array.next = array.next

        array = array.next
    return glue(quickersort(lower_array_to_sort.next), equal_before_sort.next, quickersort(higher_array_to_sort.next))
