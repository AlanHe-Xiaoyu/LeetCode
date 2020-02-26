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
    public List<Integer> inorderTraversal(TreeNode root) {

        """
        Soln #1 - Recursive
        Runtime: 0 ms, faster than 100.00% of Java online submissions for Binary Tree Inorder Traversal.
        Memory Usage: 37.6 MB, less than 5.11% of Java online submissions for Binary Tree Inorder Traversal.
        """
        if (root == null) {
            return new ArrayList<Integer>();
        }
        List<Integer> result = inorderTraversal(root.left);
        result.add(root.val);
        result.addAll(inorderTraversal(root.right));
        return result;



        """
        Soln #2 - Iterative
        Runtime: 0 ms, faster than 100.00% of Java online submissions for Binary Tree Inorder Traversal.
        Memory Usage: 37.7 MB, less than 5.11% of Java online submissions for Binary Tree Inorder Traversal.
        """
        List<Integer> result = new ArrayList<>();
        Stack<TreeNode> stack = new Stack<>();
        
        TreeNode cur = root;
        while (cur != null || !stack.isEmpty()) {
            while (cur != null) {
                stack.push(cur);
                cur = cur.left;
            }
            cur = stack.pop();
            result.add(cur.val);
            cur = cur.right;
        }
        
        return result;
    }
}