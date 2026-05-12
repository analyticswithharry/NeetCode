//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 218 -- Minimum Height Trees
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 109
// =============================================================
//
// QUESTION:
//   Given an undirected tree, find roots that produce minimum-height trees (peel leaves BFS).
// =============================================================
package main
import "fmt"
func findMHT(n int, e [][]int) []int { if n==1 { return []int{0} }; g:=make([]map[int]bool,n); d:=make([]int,n); for i:=range g { g[i]=map[int]bool{} }; for _,x:=range e { g[x[0]][x[1]]=true; g[x[1]][x[0]]=true; d[x[0]]++; d[x[1]]++ }; q:=[]int{}; for i:=0;i<n;i++ { if d[i]==1 { q=append(q,i) } }; rem:=n; for rem>2 { rem-=len(q); nq:=[]int{}; for _,x:=range q { for y:=range g[x] { d[y]--; if d[y]==1 { nq=append(nq,y) } } }; q=nq }; return q }
func main(){ fmt.Println(findMHT(6,[][]int{{3,0},{3,1},{3,2},{3,4},{5,4}})) }
