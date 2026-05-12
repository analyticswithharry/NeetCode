// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 234 -- Reverse Nodes In K Group
// Category   : Linked List
// Difficulty : Hard
// Study Plan : Day 117
// =============================================================
//
// QUESTION:
//   Reverse nodes in groups of k. Remaining tail stays.
// =============================================================
class N{constructor(v,n=null){this.v=v;this.n=n;}}
function reverseK(head,k){const d=new N(0);d.n=head;let g=d;while(true){let kth=g;for(let i=0;i<k;i++){kth=kth.n;if(!kth)return d.n;}const nxt=kth.n;let pre=nxt,cur=g.n;while(cur!==nxt){const t=cur.n;cur.n=pre;pre=cur;cur=t;}const tmp=g.n;g.n=kth;g=tmp;}}
function to(a){const d=new N(0);let c=d;for(const x of a){c.n=new N(x);c=c.n;}return d.n;}
function out(h){const r=[];while(h){r.push(h.v);h=h.n;}return r;}
console.log(out(reverseK(to([1,2,3,4,5]),2)));
