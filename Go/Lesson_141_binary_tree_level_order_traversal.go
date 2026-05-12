//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 141 -- Binary Tree Level Order Traversal
// Category   : Trees
// Difficulty : Medium
// Study Plan : Day 71
// =============================================================
//
// QUESTION:
//   Return level-order traversal of a binary tree (values grouped by level).
// =============================================================
package main
import "fmt"
type TN struct{ Val int; L,R *TN }
func levels(root *TN) [][]int { var res [][]int; if root==nil { return res }; q:=[]*TN{root}; for len(q)>0 { var lvl []int; n:=len(q); for i:=0;i<n;i++ { x:=q[0]; q=q[1:]; lvl=append(lvl,x.Val); if x.L!=nil { q=append(q,x.L) }; if x.R!=nil { q=append(q,x.R) } }; res=append(res,lvl) }; return res }
func main(){ r:=&TN{3,&TN{9,nil,nil},&TN{20,&TN{15,nil,nil},&TN{7,nil,nil}}}; fmt.Println(levels(r)) }
