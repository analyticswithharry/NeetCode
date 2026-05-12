//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 135 -- Longest Happy String
// Category   : Heap Priority Queue
// Difficulty : Medium
// Study Plan : Day 68
// =============================================================
//
// QUESTION:
//   Given a,b,c counts of letters, build the longest string with at most a 'a', b 'b', c 'c' such that no three consecutive letters are equal.
// =============================================================
package main
import ("fmt";"container/heap")
type Item struct{ Cnt int; Ch byte }
type PQ []Item
func (p PQ) Len() int{return len(p)}; func (p PQ) Less(i,j int) bool{return p[i].Cnt>p[j].Cnt}; func (p PQ) Swap(i,j int){p[i],p[j]=p[j],p[i]}
func (p *PQ) Push(x any){*p=append(*p,x.(Item))}; func (p *PQ) Pop() any{o:=*p; n:=len(o); x:=o[n-1]; *p=o[:n-1]; return x}
func longest(a,b,c int) string { h:=&PQ{}; if a>0 { *h=append(*h,Item{a,'a'}) }; if b>0 { *h=append(*h,Item{b,'b'}) }; if c>0 { *h=append(*h,Item{c,'c'}) }; heap.Init(h); var s []byte; for h.Len()>0 { x:=heap.Pop(h).(Item); n:=len(s); if n>=2 && s[n-1]==x.Ch && s[n-2]==x.Ch { if h.Len()==0 { break }; y:=heap.Pop(h).(Item); s=append(s,y.Ch); if y.Cnt-1>0 { heap.Push(h,Item{y.Cnt-1,y.Ch}) }; heap.Push(h,x) } else { s=append(s,x.Ch); if x.Cnt-1>0 { heap.Push(h,Item{x.Cnt-1,x.Ch}) } } }; return string(s) }
func main(){ fmt.Println(longest(1,1,7)); fmt.Println(longest(7,1,0)) }
