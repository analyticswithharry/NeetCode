// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 083 -- Validate Binary Search Tree
// Category   : Trees
// Difficulty : Medium
// Study Plan : Day 42
// =============================================================
//
// QUESTION:
//   Given the root of a binary tree, determine if it is a valid BST.
// =============================================================

public class Lesson083_ValidateBinarySearchTree {
    static class TreeNode { int val; TreeNode left, right; TreeNode(int v, TreeNode l, TreeNode r){val=v; left=l; right=r;} TreeNode(int v){this(v,null,null);} }
    boolean go(TreeNode n, long lo, long hi){
        if (n == null) return true;
        if (n.val <= lo || n.val >= hi) return false;
        return go(n.left, lo, n.val) && go(n.right, n.val, hi);
    }
    public boolean isValidBST(TreeNode root){ return go(root, Long.MIN_VALUE, Long.MAX_VALUE); }
    public static void main(String[] a){
        TreeNode r = new TreeNode(2, new TreeNode(1), new TreeNode(3));
        TreeNode bad = new TreeNode(5, new TreeNode(1), new TreeNode(4, new TreeNode(3), new TreeNode(6)));
        System.out.println(new Lesson083_ValidateBinarySearchTree().isValidBST(r)+" "+new Lesson083_ValidateBinarySearchTree().isValidBST(bad));
    }
}
