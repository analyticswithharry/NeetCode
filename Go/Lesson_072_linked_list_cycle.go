//go:build ignore

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

package main
import "fmt"
type ListNode struct { Val int; Next *ListNode }
func hasCycle(head *ListNode) bool {
    slow, fast := head, head
    for fast != nil && fast.Next != nil { slow = slow.Next; fast = fast.Next.Next; if slow == fast { return true } }
    return false
}
func main(){
    a := &ListNode{Val:1}; b := &ListNode{Val:2}; c := &ListNode{Val:3}
    a.Next = b; b.Next = c; c.Next = a; fmt.Println(hasCycle(a))
    d := &ListNode{Val:1}; d.Next = &ListNode{Val:2}; fmt.Println(hasCycle(d))
}
