// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 080 -- Binary Tree Level Order Traversal
// Category   : Trees
// Difficulty : Medium
// Study Plan : Day 40
// =============================================================
//
// QUESTION:
//   Return level-order traversal of a binary tree as list of lists.
//
//   Example: [3,9,20,null,null,15,7] -> [[3],[9,20],[15,7]]
// =============================================================

function TreeNode(v,l,r){ this.val=v||0; this.left=l||null; this.right=r||null; }
var levelOrder = function(root){
    if (!root) return [];
    const out = [], q = [root];
    while (q.length){
        const lvl = [], n = q.length;
        for (let i=0;i<n;i++){ const x = q.shift(); lvl.push(x.val); if (x.left) q.push(x.left); if (x.right) q.push(x.right); }
        out.push(lvl);
    }
    return out;
};
const r = new TreeNode(3, new TreeNode(9), new TreeNode(20, new TreeNode(15), new TreeNode(7)));
console.log(levelOrder(r));
