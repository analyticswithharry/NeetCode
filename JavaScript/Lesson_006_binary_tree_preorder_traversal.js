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

function TreeNode(v, l, r) { this.val = v ?? 0; this.left = l ?? null; this.right = r ?? null; }

var preorderTraversal = function(root) {
    if (!root) return [];
    const out = [], st = [root];
    while (st.length) {
        const n = st.pop(); out.push(n.val);
        if (n.right) st.push(n.right);
        if (n.left)  st.push(n.left);
    }
    return out;
};

console.log(preorderTraversal(new TreeNode(1, null, new TreeNode(2, new TreeNode(3)))));
