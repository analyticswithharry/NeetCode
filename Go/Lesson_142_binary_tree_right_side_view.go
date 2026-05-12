//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 142 -- Binary Tree Right Side View
// Category   : Trees
// Difficulty : Medium
// Study Plan : Day 71
// =============================================================
//
// QUESTION:
//   Return values seen from the right side of a binary tree.
// =============================================================
package main
import "fmt"
type TN struct{ Val int; L,R *TN }
func view(root *TN) []int { if root==nil { return nil }; q:=[]*TN{root}; var res []int; for len(q)>0 { n:=len(q); for i:=0;i<n;i++ { x:=q[0]; q=q[1:]; if i==n-1 { res=append(res,x.Val) }; if x.L!=nil { q=append(q,x.L) }; if x.R!=nil { q=append(q,x.R) } } }; return res }
func main(){ r:=&TN{1,&TN{2,nil,&TN{5,nil,nil}},&TN{3,nil,&TN{4,nil,nil}}}; fmt.Println(view(r)) }
