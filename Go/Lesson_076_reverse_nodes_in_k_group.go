//go:build ignore

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

package main
import "fmt"
type ListNode struct { Val int; Next *ListNode }
func reverseKGroup(head *ListNode, k int) *ListNode {
    cur := head; cnt := 0
    for cur != nil && cnt < k { cur = cur.Next; cnt++ }
    if cnt < k { return head }
    var prev *ListNode = nil; cur = head
    for i := 0; i < k; i++ { n := cur.Next; cur.Next = prev; prev = cur; cur = n }
    head.Next = reverseKGroup(cur, k)
    return prev
}
func fromArr(a []int) *ListNode { d := &ListNode{}; c := d; for _,x := range a { c.Next = &ListNode{Val:x}; c = c.Next }; return d.Next }
func main(){ r := reverseKGroup(fromArr([]int{1,2,3,4,5}), 2); for r != nil { fmt.Print(r.Val," "); r = r.Next }; fmt.Println()
    s := reverseKGroup(fromArr([]int{1,2,3,4,5}), 3); for s != nil { fmt.Print(s.Val," "); s = s.Next }; fmt.Println() }
