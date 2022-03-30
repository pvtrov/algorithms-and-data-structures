"""
You are given the head of a linked list, which contains a series of integers separated by 0's. The beginning and end of the linked list will have Node.val == 0.

For every two consecutive 0's, merge all the nodes lying in between them into a single node whose value is the sum of all the merged nodes. The modified list should not contain any 0's.

Return the head of the modified linked list.
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

    def mergeNodes(self, head):
        result_head = head
        helping_head = head.next

        while helping_head is not None:
            new_value = 0
            while helping_head.val != 0:
                new_value += helping_head.val
                helping_head = helping_head.next

            head.val = new_value
            if helping_head.next is None:
                head.next = None
                return result_head
            head.next = helping_head
            head = head.next
            helping_head = helping_head.next

        return result_head


array = [0, 1, 3, 0, 4, 5, 2, 0]
x = Solution
print(x.mergeNodes(x, x.tab_to_list(x, array)))