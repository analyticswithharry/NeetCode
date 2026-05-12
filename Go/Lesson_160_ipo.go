//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 160 -- IPO
// Category   : Heap Priority Queue
// Difficulty : Hard
// Study Plan : Day 80
// =============================================================
//
// QUESTION:
//   Pick at most k projects with capital >= w each. Each project gives profit; w grows. Maximize final w.
// =============================================================
package main
import ("fmt";"sort";"container/heap")
type IH []int
func (h IH) Len() int{return len(h)}; func (h IH) Less(i,j int) bool{return h[i]>h[j]}; func (h IH) Swap(i,j int){h[i],h[j]=h[j],h[i]}
func (h *IH) Push(x any){*h=append(*h,x.(int))}; func (h *IH) Pop() any{o:=*h; n:=len(o); x:=o[n-1]; *h=o[:n-1]; return x}
func ipo(k,w int, p,c []int) int { n:=len(p); proj:=make([][2]int,n); for i:=0;i<n;i++ { proj[i]=[2]int{c[i],p[i]} }; sort.Slice(proj,func(i,j int) bool{return proj[i][0]<proj[j][0]}); h:=&IH{}; i:=0; for s:=0;s<k;s++ { for i<n && proj[i][0]<=w { heap.Push(h,proj[i][1]); i++ }; if h.Len()==0 { break }; w+=heap.Pop(h).(int) }; return w }
func main(){ fmt.Println(ipo(2,0,[]int{1,2,3},[]int{0,1,1})); fmt.Println(ipo(3,0,[]int{1,2,3},[]int{0,1,2})) }
