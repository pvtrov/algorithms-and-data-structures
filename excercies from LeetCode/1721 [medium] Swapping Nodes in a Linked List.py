"""
You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from
the end (the list is 1-indexed).
"""


class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


class Solution:
    def tab_to_list(self, array):
        h = ListNode()
        c = h
        for i in range(len(array)):
            x = ListNode()
            x.val = array[i]
            c.next = x
            c = x

        return h.next

    def swapNodes(self, head, k):
        dummy = head
        solver = head
        getting_values = head
        counter = 0
        solving_counter = 0

        while dummy:
            counter += 1
            dummy = dummy.next
        second_elem = counter - k + 1

        if counter == 1 or second_elem == k:
            return head

        while getting_values:
            solving_counter += 1
            if solving_counter == k:
                first_value = getting_values.val
            elif solving_counter == second_elem:
                second_value = getting_values.val
            getting_values = getting_values.next

        solving_counter = 0
        while solver:
            solving_counter += 1
            if solving_counter == k:
                solver.val = second_value
            elif solving_counter == second_elem:
                solver.val = first_value
            solver = solver.next
        return head


x = Solution
array = [1, 2, 3]
k = 2

print(x.swapNodes(x, x.tab_to_list(x, array), k))