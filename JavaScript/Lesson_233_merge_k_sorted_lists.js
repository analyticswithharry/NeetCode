// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 233 -- Merge K Sorted Lists
// Category   : Linked List
// Difficulty : Hard
// Study Plan : Day 117
// =============================================================
//
// QUESTION:
//   Merge K sorted linked lists into one. Use heap.
// =============================================================
class N{constructor(v,n=null){this.v=v;this.n=n;}}
function mergeK(lists){const arr=[];for(const L of lists){let c=L;while(c){arr.push(c.v);c=c.n;}}arr.sort((a,b)=>a-b);const d=new N(0);let c=d;for(const v of arr){c.n=new N(v);c=c.n;}return d.n;}
function to(a){const d=new N(0);let c=d;for(const x of a){c.n=new N(x);c=c.n;}return d.n;}
function out(h){const r=[];while(h){r.push(h.v);h=h.n;}return r;}
console.log(out(mergeK([to([1,4,5]),to([1,3,4]),to([2,6])])));
