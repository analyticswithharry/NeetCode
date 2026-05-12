// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 079 -- Subtree of Another Tree
// Category   : Trees
// Difficulty : Easy
// Study Plan : Day 40
// =============================================================
//
// QUESTION:
//   Given roots of two trees root and subRoot, return true if subRoot is a subtree of root.
// =============================================================

function TreeNode(v,l,r){ this.val=v||0; this.left=l||null; this.right=r||null; }
const same = (p,q) => !p && !q ? true : (!p||!q||p.val!==q.val ? false : same(p.left,q.left)&&same(p.right,q.right));
var isSubtree = function(root, sub){
    if (!root) return false;
    if (same(root, sub)) return true;
    return isSubtree(root.left, sub) || isSubtree(root.right, sub);
};
const r = new TreeNode(3, new TreeNode(4, new TreeNode(1), new TreeNode(2)), new TreeNode(5));
const s = new TreeNode(4, new TreeNode(1), new TreeNode(2));
console.log(isSubtree(r, s));
