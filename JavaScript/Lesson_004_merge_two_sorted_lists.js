// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 004 -- Merge Two Sorted Lists
// Category   : Linked List
// Difficulty : Easy
// Study Plan : Day 2
// =============================================================
//
// QUESTION:
//   You are given the heads of two sorted linked lists list1 and list2.
//   Merge them into one sorted list and return its head.
//
//   Example:
//     Input : 1->2->4, 1->3->4
//     Output: 1->1->2->3->4->4
// =============================================================

function ListNode(val, next) { this.val = val ?? 0; this.next = next ?? null; }

var mergeTwoLists = function(a, b) {
    const d = new ListNode(); let t = d;
    while (a && b) {
        if (a.val <= b.val) { t.next = a; a = a.next; }
        else { t.next = b; b = b.next; }
        t = t.next;
    }
    t.next = a || b;
    return d.next;
};

const build = vs => { const d = new ListNode(); let t = d; for (const v of vs) { t.next = new ListNode(v); t = t.next; } return d.next; };
const toArr = h => { const r = []; while (h) { r.push(h.val); h = h.next; } return r; };
console.log(toArr(mergeTwoLists(build([1,2,4]), build([1,3,4]))));
