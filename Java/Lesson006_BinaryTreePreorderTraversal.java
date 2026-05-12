// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 006 -- Binary Tree Preorder Traversal
// Category   : Trees
// Difficulty : Easy
// Study Plan : Day 3
// =============================================================
//
// QUESTION:
//   Given the root of a binary tree, return the preorder (Root, Left, Right)
//   traversal of its nodes' values.
//
//   Example:
//     Input : root = [1,null,2,3]
//     Output: [1, 2, 3]
// =============================================================

import java.util.*;

public class Lesson006_BinaryTreePreorderTraversal {
    static class TreeNode { int val; TreeNode left, right; TreeNode(int v){val=v;} }

    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> out = new ArrayList<>();
        if (root == null) return out;
        Deque<TreeNode> st = new ArrayDeque<>(); st.push(root);
        while (!st.isEmpty()) {
            TreeNode n = st.pop(); out.add(n.val);
            if (n.right != null) st.push(n.right);
            if (n.left  != null) st.push(n.left);
        }
        return out;
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(1); root.right = new TreeNode(2); root.right.left = new TreeNode(3);
        System.out.println(new Lesson006_BinaryTreePreorderTraversal().preorderTraversal(root));
    }
}
