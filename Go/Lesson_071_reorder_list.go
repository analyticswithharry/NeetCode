//go:build ignore

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

package main
import "fmt"
type ListNode struct { Val int; Next *ListNode }
func reorderList(head *ListNode) {
    if head == nil || head.Next == nil { return }
    slow, fast := head, head
    for fast.Next != nil && fast.Next.Next != nil { slow = slow.Next; fast = fast.Next.Next }
    var prev *ListNode = nil; cur := slow.Next; slow.Next = nil
    for cur != nil { n := cur.Next; cur.Next = prev; prev = cur; cur = n }
    l1, l2 := head, prev
    for l2 != nil { t1, t2 := l1.Next, l2.Next; l1.Next = l2; l2.Next = t1; l1, l2 = t1, t2 }
}
func fromArr(a []int) *ListNode { d := &ListNode{}; c := d; for _,x := range a { c.Next = &ListNode{Val:x}; c = c.Next }; return d.Next }
func main(){ h := fromArr([]int{1,2,3,4}); reorderList(h); for h != nil { fmt.Print(h.Val," "); h = h.Next }; fmt.Println() }
