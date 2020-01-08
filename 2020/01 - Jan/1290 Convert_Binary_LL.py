# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # head: ListNode
    def getDecimalValue(self, head) -> int:

        """
        Runtime: 28 ms, faster than 66.59% of Python3 online submissions for Convert Binary Number in a Linked List to Integer.
        Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Convert Binary Number in a Linked List to Integer.
        """
        val = 0
        while head is not None:
            val = val * 2 + head.val
            head = head.next
        return val