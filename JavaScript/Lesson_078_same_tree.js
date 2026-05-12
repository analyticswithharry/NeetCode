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

function TreeNode(v,l,r){ this.val=v||0; this.left=l||null; this.right=r||null; }
var isSameTree = function(p, q){
    if (!p && !q) return true;
    if (!p || !q || p.val !== q.val) return false;
    return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
};
const a = new TreeNode(1, new TreeNode(2), new TreeNode(3));
const b = new TreeNode(1, new TreeNode(2), new TreeNode(3));
const c = new TreeNode(1, new TreeNode(2));
console.log(isSameTree(a,b), isSameTree(a,c));
