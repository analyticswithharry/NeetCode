// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 141 -- Binary Tree Level Order Traversal
// Category   : Trees
// Difficulty : Medium
// Study Plan : Day 71
// =============================================================
//
// QUESTION:
//   Return level-order traversal of a binary tree (values grouped by level).
// =============================================================
class TN{constructor(v,l=null,r=null){this.val=v;this.left=l;this.right=r;}}
function levels(root){if(!root)return [];const q=[root],res=[];while(q.length){const lvl=[];const n=q.length;for(let i=0;i<n;i++){const x=q.shift();lvl.push(x.val);if(x.left)q.push(x.left);if(x.right)q.push(x.right);}res.push(lvl);}return res;}
const r=new TN(3,new TN(9),new TN(20,new TN(15),new TN(7)));
console.log(JSON.stringify(levels(r)));
