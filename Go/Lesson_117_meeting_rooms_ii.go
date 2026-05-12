//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 117 -- Meeting Rooms II
// Category   : Intervals
// Difficulty : Medium
// Study Plan : Day 59
// =============================================================
//
// QUESTION:
//   Given an array of meeting time intervals, return the minimum number of conference rooms required.
// =============================================================
package main
import ("fmt";"sort";"container/heap")
type IH []int
func (h IH) Len() int{return len(h)}; func (h IH) Less(i,j int) bool{return h[i]<h[j]}; func (h IH) Swap(i,j int){h[i],h[j]=h[j],h[i]}
func (h *IH) Push(x any){*h=append(*h,x.(int))}; func (h *IH) Pop() any{o:=*h; n:=len(o); x:=o[n-1]; *h=o[:n-1]; return x}
func minRooms(it [][]int) int { sort.Slice(it,func(i,j int) bool{return it[i][0]<it[j][0]}); h:=&IH{}; heap.Init(h); for _,x:=range it { if h.Len()>0 && (*h)[0]<=x[0] { heap.Pop(h) }; heap.Push(h,x[1]) }; return h.Len() }
func main(){ fmt.Println(minRooms([][]int{{0,30},{5,10},{15,20}})); fmt.Println(minRooms([][]int{{7,10},{2,4}})) }
