// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 085 -- Construct Binary Tree from Preorder and Inorder
// Category   : Trees
// Difficulty : Medium
// Study Plan : Day 43
// =============================================================
//
// QUESTION:
//   Given preorder and inorder traversals of a binary tree (no duplicates), construct and return the tree.
// =============================================================

import java.util.*;
public class Lesson085_ConstructBinaryTreeFromPreorderAndInorder {
    static class TreeNode { int val; TreeNode left, right; TreeNode(int v){val=v;} }
    int p = 0; Map<Integer,Integer> idx = new HashMap<>();
    TreeNode go(int[] preorder, int l, int r){
        if (l > r) return null;
        int v = preorder[p++]; TreeNode root = new TreeNode(v); int m = idx.get(v);
        root.left = go(preorder, l, m-1); root.right = go(preorder, m+1, r);
        return root;
    }
    public TreeNode buildTree(int[] preorder, int[] inorder){
        for (int i=0;i<inorder.length;i++) idx.put(inorder[i], i);
        return go(preorder, 0, inorder.length-1);
    }
    static List<Integer> pre(TreeNode n){ List<Integer> r=new ArrayList<>(); if (n==null) return r;
        r.add(n.val); r.addAll(pre(n.left)); r.addAll(pre(n.right)); return r; }
    public static void main(String[] a){
        TreeNode t = new Lesson085_ConstructBinaryTreeFromPreorderAndInorder().buildTree(new int[]{3,9,20,15,7}, new int[]{9,3,15,20,7});
        System.out.println(pre(t));
    }
}
