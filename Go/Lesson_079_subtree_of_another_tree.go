//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 079 -- Subtree of Another Tree
// Category   : Trees
// Difficulty : Easy
// Study Plan : Day 40
// =============================================================
//
// QUESTION:
//   Given roots of two trees root and subRoot, return true if subRoot is a subtree of root.
// =============================================================

package main
import "fmt"
type TreeNode struct { Val int; Left, Right *TreeNode }
func same(p, q *TreeNode) bool {
    if p == nil && q == nil { return true }
    if p == nil || q == nil || p.Val != q.Val { return false }
    return same(p.Left,q.Left) && same(p.Right,q.Right)
}
func isSubtree(root, sub *TreeNode) bool {
    if root == nil { return false }
    if same(root, sub) { return true }
    return isSubtree(root.Left, sub) || isSubtree(root.Right, sub)
}
func main(){
    r := &TreeNode{Val:3, Left:&TreeNode{Val:4, Left:&TreeNode{Val:1}, Right:&TreeNode{Val:2}}, Right:&TreeNode{Val:5}}
    s := &TreeNode{Val:4, Left:&TreeNode{Val:1}, Right:&TreeNode{Val:2}}
    fmt.Println(isSubtree(r, s))
}
