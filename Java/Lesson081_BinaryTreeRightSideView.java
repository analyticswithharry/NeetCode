// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 081 -- Binary Tree Right Side View
// Category   : Trees
// Difficulty : Medium
// Study Plan : Day 41
// =============================================================
//
// QUESTION:
//   Return the values of nodes you'd see ordered from top to bottom from the right side.
//
//   Example: [1,2,3,null,5,null,4] -> [1,3,4]
// =============================================================

import java.util.*;
public class Lesson081_BinaryTreeRightSideView {
    static class TreeNode { int val; TreeNode left, right; TreeNode(int v, TreeNode l, TreeNode r){val=v; left=l; right=r;} TreeNode(int v){this(v,null,null);} }
    public List<Integer> rightSideView(TreeNode root){
        List<Integer> out = new ArrayList<>();
        if (root == null) return out;
        Deque<TreeNode> q = new ArrayDeque<>(); q.add(root);
        while (!q.isEmpty()){
            int n = q.size();
            for (int i=0;i<n;i++){ TreeNode x = q.poll(); if (i == n-1) out.add(x.val);
                if (x.left != null) q.add(x.left); if (x.right != null) q.add(x.right); }
        }
        return out;
    }
    public static void main(String[] a){
        TreeNode r = new TreeNode(1, new TreeNode(2, null, new TreeNode(5)), new TreeNode(3, null, new TreeNode(4)));
        System.out.println(new Lesson081_BinaryTreeRightSideView().rightSideView(r));
    }
}
