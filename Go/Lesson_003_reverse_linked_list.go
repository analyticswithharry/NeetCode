//go:build ignore

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

package main

import "fmt"

type ListNode struct { Val int; Next *ListNode }

func reverseList(head *ListNode) *ListNode {
    var prev *ListNode
    for head != nil { n := head.Next; head.Next = prev; prev = head; head = n }
    return prev
}

func main() {
    h := &ListNode{1, &ListNode{2, &ListNode{3, &ListNode{4, &ListNode{5, nil}}}}}
    r := reverseList(h)
    for r != nil { fmt.Print(r.Val, " "); r = r.Next }
    fmt.Println()
}
