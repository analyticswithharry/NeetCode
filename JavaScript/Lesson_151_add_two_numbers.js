// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 151 -- Add Two Numbers
// Category   : Linked List
// Difficulty : Medium
// Study Plan : Day 76
// =============================================================
//
// QUESTION:
//   Two non-empty linked lists (least-significant-digit first). Add and return sum as linked list.
// =============================================================
class LN{constructor(v,n=null){this.val=v;this.next=n;}}
function add(a,b){const d=new LN(0);let cur=d,c=0;while(a||b||c){let v=c+(a?a.val:0)+(b?b.val:0);c=Math.floor(v/10);v%=10;cur.next=new LN(v);cur=cur.next;a=a?a.next:null;b=b?b.next:null;}return d.next;}
function fromArr(a){const d=new LN(0);let c=d;for(const x of a){c.next=new LN(x);c=c.next;}return d.next;}
function toArr(n){const r=[];while(n){r.push(n.val);n=n.next;}return r;}
console.log(toArr(add(fromArr([2,4,3]),fromArr([5,6,4]))));
