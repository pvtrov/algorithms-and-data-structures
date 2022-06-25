class Node:
    def __init__(self):
        self.value = None
        self.next = None


def printlist(f):
    while f is not None:
        print(f.value, "-->", end = " ")
        f = f.next
    print("|")


def tab_to_list(array):
    h = Node()
    c = h
    for i in range(len(array)):
        x = Node()
        x.value = array[i]
        c.next = x
        c = x

    return h.next


def QuickerSort(f):
    if f is None:
        return f
    smaller = Node()
    small = smaller
    equal = Node()
    eq = equal
    greater = Node()
    great = greater

    pivot = f.value
    while f is not None:
        if f.value < pivot:
            small.next = f
            small = small.next
            eq.next = None
            great.next = None
        elif f.value == pivot:
            eq.next = f
            eq= eq.next
            small.next = None
            great.next = None
        else:
            great.next = f
            great = great.next
            eq.next = None
            small.next = None
        f = f.next
    return merge(QuickerSort(smaller.next), equal.next, QuickerSort(greater.next))


def merge(smaller, equal, greater):
    tmp = smaller
    while smaller is not None and tmp.next is not None:
        tmp = tmp.next

    tmp2 = equal
    while equal is not None and tmp2.next is not None:
        tmp2 = tmp2.next

    if smaller is not None:
        tmp.next = equal
        tmp2.next = greater
        return smaller
    else:
        tmp2.next = greater
        return equal


if __name__ == '__main__':
    array = [6, 7, 1, 2, 4, 6, 4, 8, 2, 4, 0, 9, 8, 1, 5, 7, 3, 5, 8, 9, 2, 5, 3, 4, 8]
    L = tab_to_list(array)
    sorted = QuickerSort(L)
    print(printlist(sorted))