# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """
        Runtime: 40 ms, faster than 98.17% of Python3 online submissions for Linked List Cycle.
        Memory Usage: 17 MB, less than 32.61% of Python3 online submissions for Linked List Cycle.
        """
        # Edge case, LL has 0 or 1 node -> no cycle
        if not head or not head.next:
            return False
        
        slow, fast = head, head.next
        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
            
        return False