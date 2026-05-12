//go:build ignore

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

package main

import "fmt"

type ListNode struct { Val int; Next *ListNode }

func mergeTwoLists(a, b *ListNode) *ListNode {
    d := &ListNode{}; t := d
    for a != nil && b != nil {
        if a.Val <= b.Val { t.Next = a; a = a.Next } else { t.Next = b; b = b.Next }
        t = t.Next
    }
    if a != nil { t.Next = a } else { t.Next = b }
    return d.Next
}

func build(v []int) *ListNode { d := &ListNode{}; t := d
    for _, x := range v { t.Next = &ListNode{Val:x}; t = t.Next }
    return d.Next }

func main() {
    r := mergeTwoLists(build([]int{1,2,4}), build([]int{1,3,4}))
    for r != nil { fmt.Print(r.Val, " "); r = r.Next }
    fmt.Println()
}
