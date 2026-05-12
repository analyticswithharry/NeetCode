// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 069 -- Add Two Numbers
// Category   : Linked List
// Difficulty : Medium
// Study Plan : Day 35
// =============================================================
//
// QUESTION:
//   Two non-empty linked lists representing non-negative integers in reverse order. Return sum as linked list.
//
//   Example: 2->4->3 + 5->6->4 = 7->0->8 (i.e., 342 + 465 = 807)
// =============================================================

function ListNode(v,n){ this.val=v||0; this.next=n||null; }
var addTwoNumbers = function(l1, l2){
    const dummy = new ListNode(); let cur = dummy, carry = 0;
    while (l1 || l2 || carry){
        const x = (l1?l1.val:0) + (l2?l2.val:0) + carry;
        carry = Math.floor(x/10); cur.next = new ListNode(x%10); cur = cur.next;
        l1 = l1?l1.next:null; l2 = l2?l2.next:null;
    }
    return dummy.next;
};
const fromArr = a => { const d = new ListNode(); let c = d; for (const x of a){ c.next = new ListNode(x); c = c.next; } return d.next; };
const toArr = n => { const a = []; while (n){ a.push(n.val); n = n.next; } return a; };
console.log(toArr(addTwoNumbers(fromArr([2,4,3]), fromArr([5,6,4]))));
