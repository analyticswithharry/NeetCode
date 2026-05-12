// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 080 -- Binary Tree Level Order Traversal
// Category   : Trees
// Difficulty : Medium
// Study Plan : Day 40
// =============================================================
//
// QUESTION:
//   Return level-order traversal of a binary tree as list of lists.
//
//   Example: [3,9,20,null,null,15,7] -> [[3],[9,20],[15,7]]
// =============================================================

import java.util.*;
public class Lesson080_BinaryTreeLevelOrderTraversal {
    static class TreeNode { int val; TreeNode left, right; TreeNode(int v, TreeNode l, TreeNode r){val=v; left=l; right=r;} TreeNode(int v){this(v,null,null);} }
    public List<List<Integer>> levelOrder(TreeNode root){
        List<List<Integer>> out = new ArrayList<>();
        if (root == null) return out;
        Deque<TreeNode> q = new ArrayDeque<>(); q.add(root);
        while (!q.isEmpty()){
            int n = q.size(); List<Integer> lvl = new ArrayList<>();
            for (int i=0;i<n;i++){ TreeNode x = q.poll(); lvl.add(x.val);
                if (x.left != null) q.add(x.left); if (x.right != null) q.add(x.right); }
            out.add(lvl);
        }
        return out;
    }
    public static void main(String[] a){
        TreeNode r = new TreeNode(3, new TreeNode(9), new TreeNode(20, new TreeNode(15), new TreeNode(7)));
        System.out.println(new Lesson080_BinaryTreeLevelOrderTraversal().levelOrder(r));
    }
}
