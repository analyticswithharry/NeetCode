// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 078 -- Same Tree
// Category   : Trees
// Difficulty : Easy
// Study Plan : Day 39
// =============================================================
//
// QUESTION:
//   Given two binary trees, check if they are structurally identical with same node values.
// =============================================================

public class Lesson078_SameTree {
    static class TreeNode { int val; TreeNode left, right; TreeNode(int v, TreeNode l, TreeNode r){val=v; left=l; right=r;} TreeNode(int v){this(v,null,null);} }
    public boolean isSameTree(TreeNode p, TreeNode q){
        if (p==null && q==null) return true;
        if (p==null || q==null || p.val != q.val) return false;
        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }
    public static void main(String[] a){
        TreeNode x = new TreeNode(1, new TreeNode(2), new TreeNode(3));
        TreeNode y = new TreeNode(1, new TreeNode(2), new TreeNode(3));
        TreeNode z = new TreeNode(1, new TreeNode(2), null);
        System.out.println(new Lesson078_SameTree().isSameTree(x,y)+" "+new Lesson078_SameTree().isSameTree(x,z));
    }
}
