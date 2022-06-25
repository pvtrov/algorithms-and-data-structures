"""Dane są następujące struktury:
struct Node { Node* next; int val; };
struct TwoLists { Node* even; Node* odd; };
Napisać funkcję: TwoLists split(Node* list);
Funkcja rozdziela listę na dwie: jedną zawierającą liczby parzyste i drugą zawierającą liczby
nieparzyste. Listy nie zawierają wartowników.
"""
""" przechodze po tablicy, i kazdy element przepinam do dobrej listy """


class Node():

    def __init__(self):
        self.value = None
        self.next = None


def tab_to_list(array):
    h = Node()
    c = h
    for i in range(len(array)):
        x = Node()
        x.value = array[i]
        c.next = x
        c = x

    return h.next


def print_list(list):
    while list is not None:
        print(list.value, "->", end=" ")
        list = list.next
    print("|")


def split_two_list(list):
    odd = Node()
    even = Node()
    Odd = odd
    Even = even

    while list is not None:
        if list.value % 2 == 0:
            even.next = list
            even = list
            odd.next = None
        else:
            odd.next = list
            odd = list
            even.next = None
        list = list.next

    return Odd.next, Even.next


if __name__ == '__main__':
    array = [5, 8, 7, 6, 2, 3, 4, 5, 9, 10, 2]
    list = tab_to_list(array)
    odd, even = split_two_list(list)
    print(print_list(odd), print_list(even))
