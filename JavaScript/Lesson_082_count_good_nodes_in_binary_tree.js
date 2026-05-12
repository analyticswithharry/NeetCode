// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 082 -- Count Good Nodes in Binary Tree
// Category   : Trees
// Difficulty : Medium
// Study Plan : Day 41
// =============================================================
//
// QUESTION:
//   A node X is good if no node on the path from root to X has value greater than X. Count good nodes.
//
//   Example: [3,1,4,3,null,1,5] -> 4
// =============================================================

function TreeNode(v,l,r){ this.val=v||0; this.left=l||null; this.right=r||null; }
var goodNodes = function(root){
    const dfs = (n, mx) => { if (!n) return 0;
        const c = n.val >= mx ? 1 : 0; const m = Math.max(mx, n.val);
        return c + dfs(n.left, m) + dfs(n.right, m); };
    return dfs(root, root.val);
};
const r = new TreeNode(3, new TreeNode(1, new TreeNode(3)), new TreeNode(4, new TreeNode(1), new TreeNode(5)));
console.log(goodNodes(r));
