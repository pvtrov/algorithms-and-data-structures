
"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
"""


from heapq import heapify, heappush, heappop


class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


def tab_to_list(array):
    h = ListNode()
    c = h
    for i in range(len(array)):
        x = ListNode()
        x.val = array[i]
        c.next = x
        c = x

    return h.next


def list_to_tab(list):
    tab = []
    while list:
        tab.append(list.val)
        list = list.next

    return tab


class Solution:

    def mergeKLists(self, T):
        heap = []
        heapify(heap)

        for list in T:
            node = list
            while node:
                heappush(heap, node.val)
                node = node.next

        result = ListNode(-100)
        to_result = result

        while heap:
            to_result.next = ListNode(heappop(heap), None)
            to_result = to_result.next

        return result.next


x = Solution
# array = [[1, 2, 3], [2, 4, 8], [3, 6, 8], [1, 3, 5, 6, 7]]
array = [[]]

T = []
for tab in array:
    T.append(tab_to_list(tab))

print(list_to_tab(x.mergeKLists(x, T)))