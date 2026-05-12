// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 081 -- Binary Tree Right Side View
// Category   : Trees
// Difficulty : Medium
// Study Plan : Day 41
// =============================================================
//
// QUESTION:
//   Return the values of nodes you'd see ordered from top to bottom from the right side.
//
//   Example: [1,2,3,null,5,null,4] -> [1,3,4]
// =============================================================

function TreeNode(v,l,r){ this.val=v||0; this.left=l||null; this.right=r||null; }
var rightSideView = function(root){
    if (!root) return [];
    const out = [], q = [root];
    while (q.length){
        const n = q.length;
        for (let i=0;i<n;i++){ const x = q.shift(); if (i===n-1) out.push(x.val);
            if (x.left) q.push(x.left); if (x.right) q.push(x.right); }
    }
    return out;
};
const r = new TreeNode(1, new TreeNode(2, null, new TreeNode(5)), new TreeNode(3, null, new TreeNode(4)));
console.log(rightSideView(r));
