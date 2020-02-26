/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public int maxDepth(TreeNode root) {

        """
        Runtime: 0 ms, faster than 100.00% of Java online submissions for Maximum Depth of Binary Tree.
        Memory Usage: 38.7 MB, less than 94.62% of Java online submissions for Maximum Depth of Binary Tree.
        """
        if (root == null) {
            return 0;
        }
        return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
    }
}