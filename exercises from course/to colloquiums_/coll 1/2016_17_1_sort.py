"""
Proszę zaimplementować funkcję void Sort( Node* list ), która otrzymuje na wejściu listę
liczb rzeczywistych (z wartownikiem), wygenerowaną zgodnie z rozkładem jednostajnym na
przedziale [0,10) i sortuje jej zawartość w kolejności niemalejącej. Funkcja powinna być możliwie
jak najszybsza (biorąc pod uwagę warunki zadania). Proszę oszacować złożoność
zaimplementowanej funkcji.
"""


class Node:
    def __init__(self):
        self.val = None
        self.next = None


def list_to_tab(list):
    tab = []
    while list:
        tab.append(list.val)
        list = list.next

    return tab


def tab_to_list(array):
    h = Node()
    c = h
    for i in range(len(array)):
        x = Node()
        x.val = array[i]
        c.next = x
        c = x

    return h.next


def insertion_sort(head):
    if head.next is None:
        return None

    sorted_list = head
    head = head.next
    sorted_list.next = None
    while head is not None:
        current = head
        head = head.next
        if current.val < sorted_list.val:
            current.next = sorted_list
            sorted_list = current
        else:
            search = sorted_list
            while search.next is not None and current.val > search.next.val:
                search = search.next
            current.next = search.next
            search.next = current
    return sorted_list


def sort(head):
    length = 0
    counter_head = head
    while counter_head is not None:
        length += 1
        counter_head = counter_head.next

    section = 10 / length
    buckets = [Node() for _ in range(length)]
    bucket_head = head
    while bucket_head.next is not None:
        index = int(bucket_head.val / section)
        temporary_bucket = buckets[index]
        while temporary_bucket.next is not None:
            temporary_bucket = temporary_bucket.next
        temporary_bucket.next = bucket_head
        bucket_head = bucket_head.next
        temporary_bucket = temporary_bucket.next
        temporary_bucket.next = None

    for i in range(len(buckets)):
        if buckets[i].next is not None:
            if buckets[i].next.next is None:
                buckets[i] = buckets[i].next
            else:
                buckets[i] = insertion_sort(buckets[i].next)

    final_list = buckets[0]
    helper = final_list
    for i in range(1, len(buckets)):
        if buckets[i].val is not None:
            while helper.next is not None:
                helper = helper.next
            helper.next = buckets[i]
            helper = helper.next
    return list_to_tab(final_list)



array = [0.45, 0.12, 0.98, 1.23, 5.43, 2.34, 1.89, 9.89, 5.43, 4.56, 7.89, 8.97, 1.90]
print(sort(tab_to_list(array)))
