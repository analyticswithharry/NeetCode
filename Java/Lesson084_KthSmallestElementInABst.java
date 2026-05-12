// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 084 -- Kth Smallest Element in a BST
// Category   : Trees
// Difficulty : Medium
// Study Plan : Day 42
// =============================================================
//
// QUESTION:
//   Given a BST, return the kth smallest value (1-indexed). Use inorder traversal.
// =============================================================

import java.util.*;
public class Lesson084_KthSmallestElementInABst {
    static class TreeNode { int val; TreeNode left, right; TreeNode(int v, TreeNode l, TreeNode r){val=v; left=l; right=r;} TreeNode(int v){this(v,null,null);} }
    public int kthSmallest(TreeNode root, int k){
        Deque<TreeNode> st = new ArrayDeque<>(); TreeNode cur = root;
        while (!st.isEmpty() || cur != null){
            while (cur != null){ st.push(cur); cur = cur.left; }
            cur = st.pop(); if (--k == 0) return cur.val;
            cur = cur.right;
        }
        return -1;
    }
    public static void main(String[] a){
        TreeNode r = new TreeNode(3, new TreeNode(1, null, new TreeNode(2)), new TreeNode(4));
        System.out.println(new Lesson084_KthSmallestElementInABst().kthSmallest(r, 1)+" "+new Lesson084_KthSmallestElementInABst().kthSmallest(r, 3));
    }
}
