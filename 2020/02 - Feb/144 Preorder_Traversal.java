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
    public List<Integer> preorderTraversal(TreeNode root) {

        """
        Soln #1 - Iterative
        Runtime: 0 ms, faster than 100.00% of Java online submissions for Binary Tree Preorder Traversal.
        Memory Usage: 37.6 MB, less than 5.17% of Java online submissions for Binary Tree Preorder Traversal.
        """
        List<Integer> result = new ArrayList<>();
        Stack<TreeNode> stack = new Stack<>();
        stack.push(root);
        while (!stack.isEmpty()) {
            TreeNode cur = stack.pop();
            if (cur != null) {
                result.add(cur.val);
                stack.push(cur.right);
                stack.push(cur.left);
            }
        }
        
        return result;

        """
        Recursive is trivial
        """
    }
}