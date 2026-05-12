// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 072 -- Linked List Cycle
// Category   : Linked List
// Difficulty : Easy
// Study Plan : Day 36
// =============================================================
//
// QUESTION:
//   Determine if a linked list has a cycle. Floyd's tortoise and hare.
// =============================================================

function ListNode(v,n){ this.val=v||0; this.next=n||null; }
var hasCycle = function(head){
    let slow = head, fast = head;
    while (fast && fast.next){ slow = slow.next; fast = fast.next.next; if (slow === fast) return true; }
    return false;
};
const a = new ListNode(1), b = new ListNode(2), c = new ListNode(3);
a.next=b; b.next=c; c.next=a; console.log(hasCycle(a));
const d = new ListNode(1); d.next = new ListNode(2); console.log(hasCycle(d));
