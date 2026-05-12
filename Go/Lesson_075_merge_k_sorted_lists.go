//go:build ignore

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

package main
import ("container/heap"; "fmt")
type ListNode struct { Val int; Next *ListNode }
type PQ []*ListNode
func (p PQ) Len() int { return len(p) }
func (p PQ) Less(i,j int) bool { return p[i].Val < p[j].Val }
func (p PQ) Swap(i,j int) { p[i], p[j] = p[j], p[i] }
func (p *PQ) Push(x interface{}) { *p = append(*p, x.(*ListNode)) }
func (p *PQ) Pop() interface{} { old := *p; n := len(old); x := old[n-1]; *p = old[:n-1]; return x }
func mergeKLists(lists []*ListNode) *ListNode {
    pq := &PQ{}; heap.Init(pq)
    for _, n := range lists { if n != nil { heap.Push(pq, n) } }
    d := &ListNode{}; cur := d
    for pq.Len() > 0 {
        n := heap.Pop(pq).(*ListNode); cur.Next = n; cur = n
        if n.Next != nil { heap.Push(pq, n.Next) }
    }
    return d.Next
}
func fromArr(a []int) *ListNode { d := &ListNode{}; c := d; for _,x := range a { c.Next = &ListNode{Val:x}; c = c.Next }; return d.Next }
func main(){ ls := []*ListNode{ fromArr([]int{1,4,5}), fromArr([]int{1,3,4}), fromArr([]int{2,6}) }
    r := mergeKLists(ls); for r != nil { fmt.Print(r.Val," "); r = r.Next }; fmt.Println() }
