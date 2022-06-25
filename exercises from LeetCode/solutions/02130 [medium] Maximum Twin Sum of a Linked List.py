"""
In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the
(n-1-i)th node, if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes
with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.
"""


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
    def pairSum(self, head):
        array = []
        sums = []

        while head:
            array.append(head.val)
            head = head.next

        for i in range(len(array)//2):
            sums.append(array[i] + array[len(array)-i-1])

        return max(sums)


x = Solution
array = [5, 4, 2, 1]
print(x.pairSum(x, tab_to_list(array)))