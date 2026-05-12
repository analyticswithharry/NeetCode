//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 084 -- Kth Smallest Element in a BST
// Category   : Trees
// Difficulty : Medium
// Study Plan : Day 42
// =============================================================
//
// QUESTION:
//   Given a BST, return the kth smallest value (1-indexed). Use inorder traversal.
// =============================================================

package main
import "fmt"
type TreeNode struct { Val int; Left, Right *TreeNode }
func kthSmallest(root *TreeNode, k int) int {
    st := []*TreeNode{}; cur := root
    for len(st) > 0 || cur != nil {
        for cur != nil { st = append(st, cur); cur = cur.Left }
        cur = st[len(st)-1]; st = st[:len(st)-1]; k--
        if k == 0 { return cur.Val }
        cur = cur.Right
    }
    return -1
}
func main(){
    r := &TreeNode{Val:3, Left:&TreeNode{Val:1, Right:&TreeNode{Val:2}}, Right:&TreeNode{Val:4}}
    fmt.Println(kthSmallest(r,1), kthSmallest(r,3))
}
