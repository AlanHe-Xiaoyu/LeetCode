import java.util.ArrayList;

class q530 {
    private class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }

    public int getMinimumDifference(TreeNode root) {
        ArrayList<Integer> iot = new ArrayList<>();
        inOrder(root, iot);

        int curMin = Integer.MAX_VALUE;
        for (int i = 0; i < iot.size() - 1; i++) {
            int diff = iot.get(i+1) - iot.get(i);
            curMin = Math.min(curMin, diff);
        }

        return curMin;
    }

    private void inOrder(TreeNode root, ArrayList<Integer> iot) {
        if (root == null) { return; }

        inOrder(root.left, iot);
        iot.add(root.val);
        inOrder(root.right, iot);
    }
}

///**
// * Definition for a binary tree node.
// * public class TreeNode {
// *     int val;
// *     TreeNode left;
// *     TreeNode right;
// *     TreeNode(int x) { val = x; }
// * }
// */
//import java.util.ArrayList;
//class Solution {
//    public int getMinimumDifference(TreeNode root) {
//        ArrayList<Integer> iot = new ArrayList<>();
//        inOrder(root, iot);
//
//        int curMin = Integer.MAX_VALUE;
//        for (int i = 0; i < iot.size() - 1; i++) {
//            int diff = iot.get(i+1) - iot.get(i);
//            curMin = Math.min(curMin, diff);
//        }
//
//        return curMin;
//    }
//
//    private void inOrder(TreeNode root, ArrayList<Integer> iot) {
//        if (root == null) { return; }
//
//        inOrder(root.left, iot);
//        iot.add(root.val);
//        inOrder(root.right, iot);
//    }
//}
