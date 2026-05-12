//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 234 -- Reverse Nodes In K Group
// Category   : Linked List
// Difficulty : Hard
// Study Plan : Day 117
// =============================================================
//
// QUESTION:
//   Reverse nodes in groups of k. Remaining tail stays.
// =============================================================
package main
import "fmt"
type N struct{v int; n *N}
func reverseK(head *N, k int) *N { d:=&N{n:head}; g:=d; for { kth:=g; for i:=0;i<k;i++ { kth=kth.n; if kth==nil { return d.n } }; nxt:=kth.n; pre,cur:=nxt,g.n; for cur!=nxt { t:=cur.n; cur.n=pre; pre=cur; cur=t }; tmp:=g.n; g.n=kth; g=tmp } }
func to(a []int) *N { d:=&N{}; c:=d; for _,x:=range a { c.n=&N{v:x}; c=c.n }; return d.n }
func main(){ r:=reverseK(to([]int{1,2,3,4,5}),2); for r!=nil { fmt.Print(r.v," "); r=r.n }; fmt.Println() }
