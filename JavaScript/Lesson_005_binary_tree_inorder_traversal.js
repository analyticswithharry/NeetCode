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

function TreeNode(v, l, r) { this.val = v ?? 0; this.left = l ?? null; this.right = r ?? null; }

var inorderTraversal = function(root) {
    const out = [], stack = []; let cur = root;
    while (cur || stack.length) {
        while (cur) { stack.push(cur); cur = cur.left; }
        cur = stack.pop(); out.push(cur.val); cur = cur.right;
    }
    return out;
};

console.log(inorderTraversal(new TreeNode(1, null, new TreeNode(2, new TreeNode(3)))));
