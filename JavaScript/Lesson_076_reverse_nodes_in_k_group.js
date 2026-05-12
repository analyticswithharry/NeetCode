// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 076 -- Reverse Nodes in k-Group
// Category   : Linked List
// Difficulty : Hard
// Study Plan : Day 38
// =============================================================
//
// QUESTION:
//   Reverse the nodes of a linked list k at a time. If fewer than k nodes remain, leave them as-is.
//
//   Example: 1->2->3->4->5, k=2 -> 2->1->4->3->5
// =============================================================

function ListNode(v,n){ this.val=v||0; this.next=n||null; }
var reverseKGroup = function(head, k){
    let cur = head, cnt = 0;
    while (cur && cnt < k){ cur = cur.next; cnt++; }
    if (cnt < k) return head;
    let prev = null; cur = head;
    for (let i=0;i<k;i++){ const n = cur.next; cur.next = prev; prev = cur; cur = n; }
    head.next = reverseKGroup(cur, k);
    return prev;
};
const fromArr = a => { const d=new ListNode(); let c=d; for (const x of a){ c.next=new ListNode(x); c=c.next; } return d.next; };
const toArr = n => { const a=[]; while (n){ a.push(n.val); n=n.next; } return a; };
console.log(toArr(reverseKGroup(fromArr([1,2,3,4,5]), 2)));
console.log(toArr(reverseKGroup(fromArr([1,2,3,4,5]), 3)));
