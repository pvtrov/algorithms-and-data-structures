"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
"""

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head):
        result_head = head

        if head is not None:
            while head.next is not None:
                while head.next.val == head.val and head.next.next is not None:
                    head.next = head.next.next
                if head.next.val == head.val and head.next.next is None:
                    head.next = None
                    return result_head
                head = head.next

