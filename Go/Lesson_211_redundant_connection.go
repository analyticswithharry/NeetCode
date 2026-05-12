//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 211 -- Redundant Connection
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 106
// =============================================================
//
// QUESTION:
//   Given an n-node tree with one extra edge (forming exactly one cycle), return the edge that can be removed.
// =============================================================
package main
import "fmt"
func findRedundant(e [][]int) []int { p:=make([]int,len(e)+1); for i:=range p{p[i]=i}; var f func(int) int; f=func(x int) int{ for p[x]!=x { p[x]=p[p[x]]; x=p[x] }; return x }; for _,x:=range e { ra,rb:=f(x[0]),f(x[1]); if ra==rb { return x }; p[ra]=rb }; return nil }
func main(){ fmt.Println(findRedundant([][]int{{1,2},{1,3},{2,3}})) }
