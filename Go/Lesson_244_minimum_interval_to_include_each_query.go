//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 244 -- Minimum Interval to Include Each Query
// Category   : Intervals
// Difficulty : Hard
// Study Plan : Day 122
// =============================================================
//
// QUESTION:
//   For each query q, find smallest interval covering q.
// =============================================================
package main
import ("container/heap";"fmt";"sort")
type item struct{sz,end int}
type pq []item
func (h pq) Len() int{return len(h)}
func (h pq) Less(i,j int) bool {return h[i].sz<h[j].sz}
func (h pq) Swap(i,j int){h[i],h[j]=h[j],h[i]}
func (h *pq) Push(x any){*h=append(*h,x.(item))}
func (h *pq) Pop() any { o:=*h; x:=o[len(o)-1]; *h=o[:len(o)-1]; return x }
func minInterval(iv [][]int, q []int) []int { sort.Slice(iv,func(i,j int) bool {return iv[i][0]<iv[j][0]}); idx:=make([]int,len(q)); for i:=range idx{idx[i]=i}; sort.Slice(idx,func(a,b int) bool {return q[idx[a]]<q[idx[b]]}); res:=make([]int,len(q)); h:=&pq{}; heap.Init(h); i:=0; for _,k:=range idx { v:=q[k]; for i<len(iv)&&iv[i][0]<=v { heap.Push(h,item{iv[i][1]-iv[i][0]+1,iv[i][1]}); i++ }; for h.Len()>0 && (*h)[0].end<v { heap.Pop(h) }; if h.Len()==0 { res[k]=-1 } else { res[k]=(*h)[0].sz } }; return res }
func main(){ fmt.Println(minInterval([][]int{{1,4},{2,4},{3,6},{4,4}},[]int{2,3,4,5})) }
