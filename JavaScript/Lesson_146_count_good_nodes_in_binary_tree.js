// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 146 -- Count Good Nodes In Binary Tree
// Category   : Trees
// Difficulty : Medium
// Study Plan : Day 73
// =============================================================
//
// QUESTION:
//   A node is good if no node on the root-to-node path has a value greater. Count good nodes.
// =============================================================
class TN{constructor(v,l=null,r=null){this.val=v;this.left=l;this.right=r;}}
function good(root){function rec(n,m){if(!n)return 0;const c=n.val>=m?1:0;return c+rec(n.left,Math.max(m,n.val))+rec(n.right,Math.max(m,n.val));}return rec(root,-Infinity);}
const r=new TN(3,new TN(1,new TN(3)),new TN(4,new TN(1),new TN(5)));
console.log(good(r));
