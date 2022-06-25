"""
Napisać funkcję: TwoLists split(Node* list);
Funkcja rozdziela listę na dwie: jedną zawierającą liczby parzyste i drugą zawierającą liczby
nieparzyste. Listy nie zawierają wartowników.
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


def TwoLists(test_case):
    head = tab_to_list(test_case)
    odd = Node()
    even = Node()
    odd_ = odd
    even_ = even

    while head is not None:
        if head.val%2 == 0:
            even.next = Node()
            even.next.val = head.val
            even = even.next
        else:
            odd.next = Node()
            odd.next.val = head.val
            odd = odd.next
        head = head.next

    odd_ = list_to_tab(odd_.next)
    even_ = list_to_tab(even_.next)
    return odd_, even_, len(odd_), len(even_), len(test_case)


test_case = [1, 5, 3, 6, 1, 6, 9, 3, 6, 2, 9, 8, 2, 6, 4, 8, 1, 5, 8, 2, 4, 7, 1, 6, 9, 5, 8]
print((TwoLists(test_case)))