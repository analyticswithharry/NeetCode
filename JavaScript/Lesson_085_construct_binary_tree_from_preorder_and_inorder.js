// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 085 -- Construct Binary Tree from Preorder and Inorder
// Category   : Trees
// Difficulty : Medium
// Study Plan : Day 43
// =============================================================
//
// QUESTION:
//   Given preorder and inorder traversals of a binary tree (no duplicates), construct and return the tree.
// =============================================================

function TreeNode(v,l,r){ this.val=v||0; this.left=l||null; this.right=r||null; }
var buildTree = function(preorder, inorder){
    const idx = new Map(); inorder.forEach((v,i) => idx.set(v,i));
    let p = 0;
    const go = (l, r) => { if (l > r) return null;
        const v = preorder[p++]; const root = new TreeNode(v); const m = idx.get(v);
        root.left = go(l, m-1); root.right = go(m+1, r); return root; };
    return go(0, inorder.length-1);
};
const pre = n => n ? [n.val, ...pre(n.left), ...pre(n.right)] : [];
console.log(pre(buildTree([3,9,20,15,7], [9,3,15,20,7])));
