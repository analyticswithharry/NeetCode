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

function TreeNode(v,l,r){ this.val=v||0; this.left=l||null; this.right=r||null; }
var kthSmallest = function(root, k){
    const st = []; let cur = root;
    while (st.length || cur){
        while (cur){ st.push(cur); cur = cur.left; }
        cur = st.pop(); if (--k === 0) return cur.val;
        cur = cur.right;
    }
};
const r = new TreeNode(3, new TreeNode(1, null, new TreeNode(2)), new TreeNode(4));
console.log(kthSmallest(r, 1), kthSmallest(r, 3));
