// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 073 -- Copy List With Random Pointer
// Category   : Linked List
// Difficulty : Medium
// Study Plan : Day 37
// =============================================================
//
// QUESTION:
//   Deep copy a linked list where each node has next and a random pointer that may point to any node or null.
// =============================================================

function Node(v,n,r){ this.val=v; this.next=n||null; this.random=r||null; }
var copyRandomList = function(head){
    if (!head) return null;
    const m = new Map(); let cur = head;
    while (cur){ m.set(cur, new Node(cur.val)); cur = cur.next; }
    cur = head;
    while (cur){ m.get(cur).next = m.get(cur.next) || null; m.get(cur).random = m.get(cur.random) || null; cur = cur.next; }
    return m.get(head);
};
const a = new Node(1), b = new Node(2); a.next = b; a.random = b; b.random = b;
const c = copyRandomList(a);
console.log([[c.val, c.random.val], [c.next.val, c.next.random.val]]);
