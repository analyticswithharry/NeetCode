//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 078 -- Same Tree
// Category   : Trees
// Difficulty : Easy
// Study Plan : Day 39
// =============================================================
//
// QUESTION:
//   Given two binary trees, check if they are structurally identical with same node values.
// =============================================================

package main
import "fmt"
type TreeNode struct { Val int; Left, Right *TreeNode }
func isSameTree(p, q *TreeNode) bool {
    if p == nil && q == nil { return true }
    if p == nil || q == nil || p.Val != q.Val { return false }
    return isSameTree(p.Left,q.Left) && isSameTree(p.Right,q.Right)
}
func main(){ a := &TreeNode{Val:1, Left:&TreeNode{Val:2}, Right:&TreeNode{Val:3}}
    b := &TreeNode{Val:1, Left:&TreeNode{Val:2}, Right:&TreeNode{Val:3}}
    fmt.Println(isSameTree(a,b)) }
