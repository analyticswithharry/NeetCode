// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 075 -- Merge K Sorted Lists
// Category   : Linked List
// Difficulty : Hard
// Study Plan : Day 38
// =============================================================
//
// QUESTION:
//   Merge k sorted linked lists into one sorted list.
//
//   Example: [[1,4,5],[1,3,4],[2,6]] -> 1->1->2->3->4->4->5->6
// =============================================================

function ListNode(v,n){ this.val=v||0; this.next=n||null; }
var mergeKLists = function(lists){
    const arr = []; for (const l of lists){ let n=l; while (n){ arr.push(n.val); n=n.next; } }
    arr.sort((a,b)=>a-b);
    const d = new ListNode(); let c = d; for (const x of arr){ c.next = new ListNode(x); c = c.next; }
    return d.next;
};
const fromArr = a => { const d=new ListNode(); let c=d; for (const x of a){ c.next=new ListNode(x); c=c.next; } return d.next; };
const toArr = n => { const a=[]; while (n){ a.push(n.val); n=n.next; } return a; };
console.log(toArr(mergeKLists([fromArr([1,4,5]), fromArr([1,3,4]), fromArr([2,6])])));
