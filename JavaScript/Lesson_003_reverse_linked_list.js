// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 003 -- Reverse Linked List
// Category   : Linked List
// Difficulty : Easy
// Study Plan : Day 2
// =============================================================
//
// QUESTION:
//   Given the head of a singly linked list, reverse the list and return
//   the new head.
//
//   Example:
//     Input : 1 -> 2 -> 3 -> 4 -> 5
//     Output: 5 -> 4 -> 3 -> 2 -> 1
// =============================================================

function ListNode(val, next) { this.val = val ?? 0; this.next = next ?? null; }

var reverseList = function(head) {
    let prev = null;
    while (head) { const n = head.next; head.next = prev; prev = head; head = n; }
    return prev;
};

const toArr = h => { const a = []; while (h) { a.push(h.val); h = h.next; } return a; };
const head = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))));
console.log(toArr(reverseList(head))); // [5,4,3,2,1]
