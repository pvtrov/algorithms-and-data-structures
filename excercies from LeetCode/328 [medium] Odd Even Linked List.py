"""
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even
indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.
"""

import queue

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
    def oddEvenList(self, head):
        queueue = queue.Queue()
        result = head
        counter = 0

        if head is None:
            return None

        while head.next and head.next.next:
            counter += 1
            if counter%2 != 0:
                queueue.put(ListNode(head.next.val))
                head.next = head.next.next
                head = head.next
                counter += 1

        if head.next:
            queueue.append(ListNode(head.next.val))
            head.next = None

        while not queueue.empty():
            head.next = ListNode(queueue.get().val, None)
            head = head.next

        return result


x = Solution
array = [1, 2, 3, 4, 5]
print(list_to_tab(x.oddEvenList(x, tab_to_list(array))))


