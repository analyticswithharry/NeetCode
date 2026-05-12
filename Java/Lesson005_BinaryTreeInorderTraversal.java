// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 005 -- Binary Tree Inorder Traversal
// Category   : Trees
// Difficulty : Easy
// Study Plan : Day 3
// =============================================================
//
// QUESTION:
//   Given the root of a binary tree, return the inorder (Left, Root, Right)
//   traversal of its nodes' values.
//
//   Example:
//     Input : root = [1,null,2,3]
//     Output: [1, 3, 2]
// =============================================================

import java.util.*;

public class Lesson005_BinaryTreeInorderTraversal {
    static class TreeNode { int val; TreeNode left, right; TreeNode(int v){val=v;} }

    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> out = new ArrayList<>(); Deque<TreeNode> st = new ArrayDeque<>();
        TreeNode cur = root;
        while (cur != null || !st.isEmpty()) {
            while (cur != null) { st.push(cur); cur = cur.left; }
            cur = st.pop(); out.add(cur.val); cur = cur.right;
        }
        return out;
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(1); root.right = new TreeNode(2); root.right.left = new TreeNode(3);
        System.out.println(new Lesson005_BinaryTreeInorderTraversal().inorderTraversal(root));
    }
}
