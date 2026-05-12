//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 159 -- Find Median From Data Stream
// Category   : Heap Priority Queue
// Difficulty : Hard
// Study Plan : Day 80
// =============================================================
//
// QUESTION:
//   Design MedianFinder: addNum, findMedian.
// =============================================================
package main
import ("fmt";"container/heap")
type IH []int
func (h IH) Len() int{return len(h)}; func (h IH) Less(i,j int) bool{return h[i]<h[j]}; func (h IH) Swap(i,j int){h[i],h[j]=h[j],h[i]}
func (h *IH) Push(x any){*h=append(*h,x.(int))}; func (h *IH) Pop() any{o:=*h; n:=len(o); x:=o[n-1]; *h=o[:n-1]; return x}
type MaxH struct{ IH }
func (h MaxH) Less(i,j int) bool{ return h.IH[i]>h.IH[j] }
type MedianFinder struct{ lo *MaxH; hi *IH }
func New() *MedianFinder { return &MedianFinder{&MaxH{}, &IH{}} }
func (m *MedianFinder) AddNum(x int){ heap.Push(m.lo,x); heap.Push(m.hi,heap.Pop(m.lo)); if m.hi.Len()>m.lo.Len() { heap.Push(m.lo,heap.Pop(m.hi)) } }
func (m *MedianFinder) FindMedian() float64 { if m.lo.Len()>m.hi.Len() { return float64(m.lo.IH[0]) }; return float64(m.lo.IH[0]+(*m.hi)[0])/2 }
func main(){ m:=New(); for _,x:=range []int{1,2,3}{ m.AddNum(x); fmt.Println(m.FindMedian()) } }
