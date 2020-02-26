/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {

        """
        Soln #1 - Recursive
        Runtime: 0 ms, faster than 100.00% of Java online submissions for Reverse Linked List.
        Memory Usage: 38.4 MB, less than 5.04% of Java online submissions for Reverse Linked List.
        """
        if (head == null || head.next == null) {
            return head;
        }
        ListNode reversed = reverseList(head.next);
        head.next.next = head;
        head.next = null;
        
        return reversed;

        """
        Soln #2 - Iterative
        Runtime: 0 ms, faster than 100.00% of Java online submissions for Reverse Linked List.
        Memory Usage: 38.1 MB, less than 5.04% of Java online submissions for Reverse Linked List.
        """
        ListNode prev = null;
        ListNode cur = head;
        while (cur != null) {
            ListNode temp = cur.next;
            cur.next = prev;
            prev = cur;
            cur = temp;
        }
        
        return prev;
    }
}