//go:build ignore

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

package main
import "fmt"
type ListNode struct { Val int; Next *ListNode }
func removeNthFromEnd(head *ListNode, n int) *ListNode {
    d := &ListNode{Next: head}; fast, slow := d, d
    for i := 0; i < n; i++ { fast = fast.Next }
    for fast.Next != nil { fast = fast.Next; slow = slow.Next }
    slow.Next = slow.Next.Next; return d.Next
}
func fromArr(a []int) *ListNode { d := &ListNode{}; c := d; for _,x := range a { c.Next = &ListNode{Val:x}; c = c.Next }; return d.Next }
func main(){ r := removeNthFromEnd(fromArr([]int{1,2,3,4,5}), 2); for r != nil { fmt.Print(r.Val," "); r = r.Next }; fmt.Println() }
