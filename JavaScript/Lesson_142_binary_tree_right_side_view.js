// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 142 -- Binary Tree Right Side View
// Category   : Trees
// Difficulty : Medium
// Study Plan : Day 71
// =============================================================
//
// QUESTION:
//   Return values seen from the right side of a binary tree.
// =============================================================
class TN{constructor(v,l=null,r=null){this.val=v;this.left=l;this.right=r;}}
function view(root){if(!root)return [];const q=[root],res=[];while(q.length){const n=q.length;for(let i=0;i<n;i++){const x=q.shift();if(i===n-1)res.push(x.val);if(x.left)q.push(x.left);if(x.right)q.push(x.right);}}return res;}
const r=new TN(1,new TN(2,null,new TN(5)),new TN(3,null,new TN(4)));
console.log(view(r));
