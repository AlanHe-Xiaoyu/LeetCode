# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        """
        Runtime: 44 ms, faster than 15.73% of Python3 online submissions for Merge Two Sorted Lists.
        Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Merge Two Sorted Lists.
        """
        
        res = ListNode(None)
        answer = res
        while l1 and l2:
            a1, a2 = l1.val, l2.val
            if a1 <= a2:
                node = ListNode(a1)
                res.next = node
                l1 = l1.next
            else:
                node = ListNode(a2)
                res.next = node
                l2 = l2.next
            res = res.next
            
        if l1:
            res.next = l1
        else:
            res.next = l2
            
        return answer.next