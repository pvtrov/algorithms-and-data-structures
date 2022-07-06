from heapq import heapify, heappush, heappop

from zad3testy import runtests
"""
Dana jest struktura realizująca listę jednokierunkową:
class Node:
    def __init__( self, val ):
    self.next = None
    self.val = val
Proszę napisać funkcję, która mając na wejściu ciąg tak zrealizowanych posortowanych list scala je
w jedną posortowaną listę (składającą się z tych samych elementów).
"""

class Node:
    def __init__( self, val ):
        self.next = None
        self.val = val


def merge(L):
    heap = []
    heapify(heap)

    for list in L:
        node = list
        while node:
            heappush(heap, node.val)
            node = node.next
    result = Node(-100)
    to_result = result

    while heap:
        to_result.next = Node(heappop(heap))
        to_result = to_result.next
    return result.next


runtests( merge )
