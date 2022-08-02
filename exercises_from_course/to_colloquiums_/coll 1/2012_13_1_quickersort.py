"""
Proszę zaimplementować funkcję sortującą (rosnąco) listę jednokierunkową metodą
QuickerSort. Algorytm QuickerSort to odmiana algorytmu QuickSort, w której funkcja
podziału dzieli sortowane dane według przyjętej wartości x na trzy grupy: mniejsze od x, równe
x, oraz większe od x. Następnie rekurencyjnie sortowane są grupy pierwsza i trzecia. Państwa
funkcja powinna mieć następujący prototyp:
struct Node { Node* next; int val; };
Node* QuickerSort ( Node* head )
Argumentem funkcji jest wskaźnik na głowę listy do posortowania a wynikiem powinien być
wskaźnik na głowę listy posortowanej. Sortowanie powinno polegać na porównywaniu wartości
val list oraz przepinaniu wskaźników next.
"""


class Node():
    def __init__(self):
        self.next = None
        self.val = None


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


def merge(small, equal, bigger):
    tmp = small
    while small is not None and tmp.next is not None:
        tmp = tmp.next

    tmp2 = equal
    while equal is not None and tmp2.next is not None:
        tmp2 = tmp2.next

    if small is not None:
        tmp.next = equal
        tmp2.next = bigger
        return small
    else:
        tmp2.next = bigger
        return equal


def quicker_sort(head):
    if head is None:
        return head

    smaller = Node()
    small = smaller
    equaler = Node()
    equal = equaler
    bigger = Node()
    big = bigger

    pivot = head.val
    while head is not None:
        if pivot > head.val:
            small.next = head
            small = small.next
            equal.next = None
            big.next = None
        elif pivot == head.val:
            small.next = None
            equal.next = head
            equal = equal.next
            big.next = None
        else:
            small.next = None
            equal.next = None
            big.next = head
            big = big.next
        head = head.next

    return merge(quicker_sort(smaller.next), equaler.next, quicker_sort(bigger.next))


def sort(array):
    return list_to_tab(quicker_sort(array))


array = [1, 3, 8, 9, 2, 4, 5, 4, 3, 1, 5, 2, 6]
print(sort(tab_to_list(array)))