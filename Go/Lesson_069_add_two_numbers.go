//go:build ignore

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

package main
import "fmt"
type ListNode struct { Val int; Next *ListNode }
func addTwoNumbers(l1, l2 *ListNode) *ListNode {
    dummy := &ListNode{}; cur := dummy; carry := 0
    for l1 != nil || l2 != nil || carry > 0 {
        x := carry
        if l1 != nil { x += l1.Val; l1 = l1.Next }
        if l2 != nil { x += l2.Val; l2 = l2.Next }
        carry = x/10; cur.Next = &ListNode{Val: x%10}; cur = cur.Next
    }
    return dummy.Next
}
func fromArr(a []int) *ListNode { d := &ListNode{}; c := d; for _,x := range a { c.Next = &ListNode{Val:x}; c = c.Next }; return d.Next }
func main(){ r := addTwoNumbers(fromArr([]int{2,4,3}), fromArr([]int{5,6,4}))
    for r != nil { fmt.Print(r.Val, " "); r = r.Next }; fmt.Println() }
