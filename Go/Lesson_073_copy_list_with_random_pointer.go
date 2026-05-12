//go:build ignore

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

package main
import "fmt"
type Node struct { Val int; Next, Random *Node }
func copyRandomList(head *Node) *Node {
    if head == nil { return nil }
    m := map[*Node]*Node{}
    for c := head; c != nil; c = c.Next { m[c] = &Node{Val: c.Val} }
    for c := head; c != nil; c = c.Next { m[c].Next = m[c.Next]; m[c].Random = m[c.Random] }
    return m[head]
}
func main(){
    a := &Node{Val:1}; b := &Node{Val:2}; a.Next = b; a.Random = b; b.Random = b
    c := copyRandomList(a)
    fmt.Println(c.Val, c.Random.Val, c.Next.Val, c.Next.Random.Val)
}
