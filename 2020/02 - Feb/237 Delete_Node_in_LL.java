/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public void deleteNode(ListNode node) {

        """
        Runtime: 0 ms, faster than 100.00% of Java online submissions for Delete Node in a Linked List.
        Memory Usage: 40.4 MB, less than 5.09% of Java online submissions for Delete Node in a Linked List.
        """
        if (node == null || node.next == null) {
            return;
        }
        
        node.val = node.next.val;
        node.next = node.next.next;
    }
}