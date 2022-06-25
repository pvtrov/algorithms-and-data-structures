"""
Proszę zaimplementować funkcję Node* fixSortedList( Node* L ), która otrzymuje na
wejściu listę jednokierunkową bez wartowanika. Lista ta jest prawie posortowana w tym sensie, że
powstała z listy posortowanej przez zmianę jednego losowo wybranego elementu na losową
wartość. Funkcja powinna przepiąć elementy listy tak, by lista stała się posortowana i zwrócić
wskaźnik do głowy tej listy. Można założyć, że wszystkie liczby na liście są różne i że lista ma co
najmniej dwa elementy. Funkcja powinna działać w czasie liniowym względem długości listy
wejściowej.
"""


class Node():
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


def fix_sorted_list(head):
    result = head
    to_pin_in = head

    while head.next is not None:
        if head.next.val < head.val:
            node_to_pin = head.next
            head.next = head.next.next
            break
        else:
            head = head.next

    while to_pin_in.next is not None:
        if node_to_pin.val > to_pin_in.next.val:
            to_pin_in = to_pin_in.next
        else:
            node_to_pin.next = to_pin_in.next
            to_pin_in.next = node_to_pin
            break
    return list_to_tab(result)


tab = [1, 3, 5, 6, 2, 7, 8, 9]
print(fix_sorted_list(tab_to_list(tab)))