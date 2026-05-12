// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 082 -- Count Good Nodes in Binary Tree
// Category   : Trees
// Difficulty : Medium
// Study Plan : Day 41
// =============================================================
//
// QUESTION:
//   A node X is good if no node on the path from root to X has value greater than X. Count good nodes.
//
//   Example: [3,1,4,3,null,1,5] -> 4
// =============================================================

public class Lesson082_CountGoodNodesInBinaryTree {
    static class TreeNode { int val; TreeNode left, right; TreeNode(int v, TreeNode l, TreeNode r){val=v; left=l; right=r;} TreeNode(int v){this(v,null,null);} }
    int dfs(TreeNode n, int mx){ if (n == null) return 0;
        int c = n.val >= mx ? 1 : 0; int m = Math.max(mx, n.val);
        return c + dfs(n.left, m) + dfs(n.right, m); }
    public int goodNodes(TreeNode root){ return dfs(root, root.val); }
    public static void main(String[] a){
        TreeNode r = new TreeNode(3, new TreeNode(1, new TreeNode(3), null), new TreeNode(4, new TreeNode(1), new TreeNode(5)));
        System.out.println(new Lesson082_CountGoodNodesInBinaryTree().goodNodes(r));
    }
}
