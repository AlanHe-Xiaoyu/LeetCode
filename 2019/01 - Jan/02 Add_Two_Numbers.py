# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        # Soln 1
        # @time = 180 ms
        num1 = l1.val
        num2 = l2.val
        k = 10
        while l1.next is not None:
            l1 = l1.next
            num1 += k * l1.val
            k *= 10

        k = 10
        while l2.next is not None:
            l2 = l2.next
            num2 += k * l2.val
            k *= 10

        total = num1 + num2
        out = ListNode(total % 10)
        pointer = out
        while total // 10:
            total = total // 10
            pointer.next = ListNode(total % 10)
            pointer = pointer.next
            
        return out



        # Soln 2 - Directly add nums in l1 into l2 (Destructive for saving space)
        # @time = 156 ms
        # @complexity O(?)
        total = l2
        carry = 0
        
        while l1:
            cur = carry + l1.val + l2.val
            carry = cur // 10
            l2.val = cur % 10

            if carry and l1.next is None:
                l1.next = ListNode(0)
                l2.next = ListNode(0)
            elif l1.next and l2.next is None:
                l2.next = ListNode(0)

            l1 = l1.next
            l2 = l2.next
        
        return total