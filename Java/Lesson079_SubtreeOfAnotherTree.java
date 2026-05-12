// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 079 -- Subtree of Another Tree
// Category   : Trees
// Difficulty : Easy
// Study Plan : Day 40
// =============================================================
//
// QUESTION:
//   Given roots of two trees root and subRoot, return true if subRoot is a subtree of root.
// =============================================================

public class Lesson079_SubtreeOfAnotherTree {
    static class TreeNode { int val; TreeNode left, right; TreeNode(int v, TreeNode l, TreeNode r){val=v; left=l; right=r;} TreeNode(int v){this(v,null,null);} }
    boolean same(TreeNode p, TreeNode q){
        if (p==null && q==null) return true;
        if (p==null || q==null || p.val != q.val) return false;
        return same(p.left,q.left) && same(p.right,q.right);
    }
    public boolean isSubtree(TreeNode root, TreeNode sub){
        if (root == null) return false;
        if (same(root, sub)) return true;
        return isSubtree(root.left, sub) || isSubtree(root.right, sub);
    }
    public static void main(String[] a){
        TreeNode r = new TreeNode(3, new TreeNode(4, new TreeNode(1), new TreeNode(2)), new TreeNode(5));
        TreeNode s = new TreeNode(4, new TreeNode(1), new TreeNode(2));
        System.out.println(new Lesson079_SubtreeOfAnotherTree().isSubtree(r, s));
    }
}
