from zad3testy import runtests
from math import inf

"""
Proszę napisać funkcję, która mając na wejściu ciąg tak zrealizowanych posortowanych list scala je
w jedną posortowaną listę (składającą się z tych samych elementów)."""


"""
by zopytamlizowac mergowanie to dla kazdej z list "ucinam elemnet i szukam odpowiednieniego miesca w tablicy result, 
gdy juz znajde odpowiednie miejsce to zamiast przechodzic po liscie resultowej jeszcze raz ide dlaej tylko kolejnym 
elementem z listy wstawijacej
złożoność czasowa: O(n-1), < po liscie resultowej przechodze n-1 razy >
pamieciowa: dodatkowe O(n) pamieci 
"""


class Node:
    def __init__(self, value):
        self.next = None
        self.val = value


def copy_val(node):
    return Node(node.val)


def merging(T):  # T to przekazane głowy tych list
    start = inf
    for i in range(len(T)):
        if T[i].val < start:
            start = T[i].val
            index = i

    result = T[index]
    head = result
    nexti = result.next

    for i in range(0, len(T)):
        if index != i:
            L = T[i]
            while L is not None:
                element = copy_val(L)
                if result.next is not None:
                    if result.val <= element.val <= nexti.val:
                        result.next = element
                        element.next = nexti
                        result = result.next
                        L = L.next
                    else:
                        result = result.next
                        nexti = nexti.next
                else:
                    result.next = element
                    result = result.next
                    L = L.next

        result = head
        nexti = result.next

    return head


runtests(merging)
