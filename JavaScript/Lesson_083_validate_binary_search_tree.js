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

function TreeNode(v,l,r){ this.val=v||0; this.left=l||null; this.right=r||null; }
var isValidBST = function(root){
    const go = (n, lo, hi) => { if (!n) return true;
        if (n.val <= lo || n.val >= hi) return false;
        return go(n.left, lo, n.val) && go(n.right, n.val, hi); };
    return go(root, -Infinity, Infinity);
};
const r = new TreeNode(2, new TreeNode(1), new TreeNode(3));
const bad = new TreeNode(5, new TreeNode(1), new TreeNode(4, new TreeNode(3), new TreeNode(6)));
console.log(isValidBST(r), isValidBST(bad));
