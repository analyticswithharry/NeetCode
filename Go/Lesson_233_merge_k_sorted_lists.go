//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 233 -- Merge K Sorted Lists
// Category   : Linked List
// Difficulty : Hard
// Study Plan : Day 117
// =============================================================
//
// QUESTION:
//   Merge K sorted linked lists into one. Use heap.
// =============================================================
package main
import ("container/heap";"fmt")
type N struct{v int; n *N}
type pq []*N
func (h pq) Len() int{return len(h)}
func (h pq) Less(i,j int) bool {return h[i].v<h[j].v}
func (h pq) Swap(i,j int){h[i],h[j]=h[j],h[i]}
func (h *pq) Push(x any){*h=append(*h,x.(*N))}
func (h *pq) Pop() any { o:=*h; x:=o[len(o)-1]; *h=o[:len(o)-1]; return x }
func mergeK(lists []*N) *N { h:=&pq{}; heap.Init(h); for _,L:=range lists { if L!=nil { heap.Push(h,L) } }; d:=&N{}; c:=d; for h.Len()>0 { x:=heap.Pop(h).(*N); c.n=x; c=x; if x.n!=nil { heap.Push(h,x.n) } }; return d.n }
func to(a []int) *N { d:=&N{}; c:=d; for _,x:=range a { c.n=&N{v:x}; c=c.n }; return d.n }
func main(){ r:=mergeK([]*N{to([]int{1,4,5}),to([]int{1,3,4}),to([]int{2,6})}); for r!=nil { fmt.Print(r.v," "); r=r.n }; fmt.Println() }
