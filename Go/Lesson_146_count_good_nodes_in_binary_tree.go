//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 146 -- Count Good Nodes In Binary Tree
// Category   : Trees
// Difficulty : Medium
// Study Plan : Day 73
// =============================================================
//
// QUESTION:
//   A node is good if no node on the root-to-node path has a value greater. Count good nodes.
// =============================================================
package main
import "fmt"
type TN struct{ Val int; L,R *TN }
func good(root *TN) int { var rec func(n *TN,m int) int; rec=func(n *TN,m int) int { if n==nil { return 0 }; c:=0; if n.Val>=m { c=1 }; nm:=m; if n.Val>nm { nm=n.Val }; return c+rec(n.L,nm)+rec(n.R,nm) }; return rec(root,-1<<31) }
func main(){ r:=&TN{3,&TN{1,&TN{3,nil,nil},nil},&TN{4,&TN{1,nil,nil},&TN{5,nil,nil}}}; fmt.Println(good(r)) }
