// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 070 -- Remove Nth Node From End of List
// Category   : Linked List
// Difficulty : Medium
// Study Plan : Day 35
// =============================================================
//
// QUESTION:
//   Remove the nth node from the end of a linked list and return its head.
//
//   Example: head = 1->2->3->4->5, n = 2 -> 1->2->3->5
// =============================================================

function ListNode(v,n){ this.val=v||0; this.next=n||null; }
var removeNthFromEnd = function(head, n){
    const d = new ListNode(0, head); let fast = d, slow = d;
    for (let i=0;i<n;i++) fast = fast.next;
    while (fast.next){ fast = fast.next; slow = slow.next; }
    slow.next = slow.next.next; return d.next;
};
const fromArr = a => { const d=new ListNode(); let c=d; for (const x of a){ c.next=new ListNode(x); c=c.next; } return d.next; };
const toArr = n => { const a=[]; while (n){ a.push(n.val); n=n.next; } return a; };
console.log(toArr(removeNthFromEnd(fromArr([1,2,3,4,5]), 2)));
