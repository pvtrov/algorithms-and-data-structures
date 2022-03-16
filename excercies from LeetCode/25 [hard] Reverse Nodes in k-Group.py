"""
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a
multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.
"""
import copy

class ListNode:
    def __init__(self, value = 0, next = None):
        self.val = value
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
    def find_kth_node(self, list, k):
        while list and k > 0:
            list = list.next
            k -= 0

        return list

    def reverseKGroup(self, head, k):












        # pointer = head
        # to_result = ListNode(0)
        # result = to_result
        #
        # while pointer:
        #     stack = []
        #     first_ptr = pointer
        #     counter = 0
        #     while first_ptr is not None and counter < k:
        #         elem = copy.deepcopy(first_ptr)
        #         elem.next = None
        #         stack.append(elem)
        #         first_ptr = first_ptr.next
        #         counter += 1
        #
        #     if first_ptr is None and counter < k:
        #         to_result.next = pointer
        #         return result.next
        #
        #     next_round = first_ptr
        #
        #     snd_counter = 0
        #     while snd_counter < k:
        #         to_result.next = stack.pop()
        #         snd_counter += 1
        #         to_result = to_result.next
        #
        #     pointer.next = next_round
        #     pointer = pointer.next
        # return result.next




x = Solution
array = [1, 2, 3, 4, 5]
print(list_to_tab(x.reverseKGroup(x, tab_to_list(array), 3)))



