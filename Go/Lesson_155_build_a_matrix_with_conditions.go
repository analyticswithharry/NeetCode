//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 155 -- Build a Matrix With Conditions
// Category   : Advanced Graphs
// Difficulty : Hard
// Study Plan : Day 78
// =============================================================
//
// QUESTION:
//   Given k rows/cols and conditions for row/col orderings, place 1..k so each appears once and conditions are satisfied. Return matrix or [].
// =============================================================
package main
import "fmt"
func topo(k int, conds [][]int) []int { adj:=make([][]int,k+1); ind:=make([]int,k+1); for _,c:=range conds { adj[c[0]]=append(adj[c[0]],c[1]); ind[c[1]]++ }; var q []int; for i:=1;i<=k;i++ { if ind[i]==0 { q=append(q,i) } }; var o []int; for len(q)>0 { x:=q[0]; q=q[1:]; o=append(o,x); for _,y:=range adj[x] { ind[y]--; if ind[y]==0 { q=append(q,y) } } }; if len(o)==k { return o }; return nil }
func build(k int, rC,cC [][]int) [][]int { r,c:=topo(k,rC),topo(k,cC); if r==nil || c==nil { return nil }; pos:=make([]int,k+1); for i,v:=range c { pos[v]=i }; g:=make([][]int,k); for i:=range g { g[i]=make([]int,k) }; for i,v:=range r { g[i][pos[v]]=v }; return g }
func main(){ fmt.Println(build(3,[][]int{{1,2},{3,2}},[][]int{{2,1},{3,2}})) }
