// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 071 -- Reorder List
// Category   : Linked List
// Difficulty : Medium
// Study Plan : Day 36
// =============================================================
//
// QUESTION:
//   Reorder L0 -> L1 -> ... -> Ln-1 -> Ln to L0 -> Ln -> L1 -> Ln-1 -> ...
//
//   Example: 1->2->3->4 -> 1->4->2->3
// =============================================================

function ListNode(v,n){ this.val=v||0; this.next=n||null; }
var reorderList = function(head){
    if (!head || !head.next) return head;
    let slow = head, fast = head;
    while (fast.next && fast.next.next){ slow = slow.next; fast = fast.next.next; }
    let prev = null, cur = slow.next; slow.next = null;
    while (cur){ const n = cur.next; cur.next = prev; prev = cur; cur = n; }
    let l1 = head, l2 = prev;
    while (l2){ const t1 = l1.next, t2 = l2.next; l1.next = l2; l2.next = t1; l1 = t1; l2 = t2; }
    return head;
};
const fromArr = a => { const d=new ListNode(); let c=d; for (const x of a){ c.next=new ListNode(x); c=c.next; } return d.next; };
const toArr = n => { const a=[]; while (n){ a.push(n.val); n=n.next; } return a; };
console.log(toArr(reorderList(fromArr([1,2,3,4]))));
console.log(toArr(reorderList(fromArr([1,2,3,4,5]))));
