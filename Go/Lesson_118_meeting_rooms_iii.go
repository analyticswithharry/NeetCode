//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 118 -- Meeting Rooms III
// Category   : Intervals
// Difficulty : Hard
// Study Plan : Day 59
// =============================================================
//
// QUESTION:
//   Given n rooms (0..n-1) and meetings [start,end], assign meetings to lowest-numbered available room, delaying if needed (preserving duration). Return room hosting most meetings.
// =============================================================
package main
import ("fmt";"sort";"container/heap")
type IH []int
func (h IH) Len() int{return len(h)}; func (h IH) Less(i,j int) bool{return h[i]<h[j]}; func (h IH) Swap(i,j int){h[i],h[j]=h[j],h[i]}
func (h *IH) Push(x any){*h=append(*h,x.(int))}; func (h *IH) Pop() any{o:=*h; n:=len(o); x:=o[n-1]; *h=o[:n-1]; return x}
type Pair struct{ T int64; R int }
type PH []Pair
func (h PH) Len() int{return len(h)}; func (h PH) Less(i,j int) bool{ if h[i].T!=h[j].T{return h[i].T<h[j].T}; return h[i].R<h[j].R }; func (h PH) Swap(i,j int){h[i],h[j]=h[j],h[i]}
func (h *PH) Push(x any){*h=append(*h,x.(Pair))}; func (h *PH) Pop() any{o:=*h; n:=len(o); x:=o[n-1]; *h=o[:n-1]; return x}
func mostBooked(n int, m [][]int) int { sort.Slice(m,func(i,j int) bool{return m[i][0]<m[j][0]}); fr:=&IH{}; for i:=0;i<n;i++{ heap.Push(fr,i) }; busy:=&PH{}; cnt:=make([]int64,n); for _,x:=range m { for busy.Len()>0 && (*busy)[0].T<=int64(x[0]) { p:=heap.Pop(busy).(Pair); heap.Push(fr,p.R) }; var r int; var e int64; if fr.Len()>0 { r=heap.Pop(fr).(int); e=int64(x[1]) } else { p:=heap.Pop(busy).(Pair); r=p.R; e=p.T+int64(x[1]-x[0]) }; heap.Push(busy,Pair{e,r}); cnt[r]++ }; mi:=0; for i:=1;i<n;i++{ if cnt[i]>cnt[mi]{ mi=i } }; return mi }
func main(){ fmt.Println(mostBooked(2,[][]int{{0,10},{1,5},{2,7},{3,4}})) }
