//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 085 -- Construct Binary Tree from Preorder and Inorder
// Category   : Trees
// Difficulty : Medium
// Study Plan : Day 43
// =============================================================
//
// QUESTION:
//   Given preorder and inorder traversals of a binary tree (no duplicates), construct and return the tree.
// =============================================================

package main
import "fmt"
type TreeNode struct { Val int; Left, Right *TreeNode }
func buildTree(preorder, inorder []int) *TreeNode {
    idx := map[int]int{}
    for i,v := range inorder { idx[v] = i }
    p := 0
    var go func(l, r int) *TreeNode
    go = func(l, r int) *TreeNode {
        if l > r { return nil }
        v := preorder[p]; p++
        root := &TreeNode{Val: v}; m := idx[v]
        root.Left = go(l, m-1); root.Right = go(m+1, r)
        return root
    }
    return go(0, len(inorder)-1)
}
func pre(n *TreeNode, out *[]int){ if n == nil { return }; *out = append(*out, n.Val); pre(n.Left, out); pre(n.Right, out) }
func main(){ t := buildTree([]int{3,9,20,15,7}, []int{9,3,15,20,7})
    out := []int{}; pre(t, &out); fmt.Println(out) }
