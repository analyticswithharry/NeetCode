//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 083 -- Validate Binary Search Tree
// Category   : Trees
// Difficulty : Medium
// Study Plan : Day 42
// =============================================================
//
// QUESTION:
//   Given the root of a binary tree, determine if it is a valid BST.
// =============================================================

package main
import ("fmt"; "math")
type TreeNode struct { Val int; Left, Right *TreeNode }
func isValidBST(root *TreeNode) bool {
    var go func(n *TreeNode, lo, hi float64) bool
    go = func(n *TreeNode, lo, hi float64) bool {
        if n == nil { return true }
        v := float64(n.Val); if v <= lo || v >= hi { return false }
        return go(n.Left, lo, v) && go(n.Right, v, hi)
    }
    return go(root, math.Inf(-1), math.Inf(1))
}
func main(){
    r := &TreeNode{Val:2, Left:&TreeNode{Val:1}, Right:&TreeNode{Val:3}}
    bad := &TreeNode{Val:5, Left:&TreeNode{Val:1}, Right:&TreeNode{Val:4, Left:&TreeNode{Val:3}, Right:&TreeNode{Val:6}}}
    fmt.Println(isValidBST(r), isValidBST(bad))
}
