"""
You are given the head of a linked list with n nodes.

For each node in the list, find the value of the next greater node. That is, for each node, find the value of the first
node that is next to it and has a strictly larger value than it.

Return an integer array answer where answer[i] is the value of the next greater node of the ith node (1-indexed). If the
ith node does not have a next greater node, set answer[i] = 0.
"""



class ListNode:
    def __init__(self, val=0, next=None):
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


    def nextLargerNodes(self, head):
        values = []
        stack = []

        while head:
            values.append(head.val)
            head = head.next
        result = [0] * len(values)

        for index, value in enumerate(values):
            while stack and values[stack[-1]] < value:
                result[stack[-1]] = value
                stack.pop()
            stack.append(index)

        return result


x = Solution
array = [3, 3]
print(x.nextLargerNodes(x, x.tab_to_list(x, array)))