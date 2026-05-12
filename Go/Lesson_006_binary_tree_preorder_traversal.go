//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 006 -- Binary Tree Preorder Traversal
// Category   : Trees
// Difficulty : Easy
// Study Plan : Day 3
// =============================================================
//
// QUESTION:
//   Given the root of a binary tree, return the preorder (Root, Left, Right)
//   traversal of its nodes' values.
//
//   Example:
//     Input : root = [1,null,2,3]
//     Output: [1, 2, 3]
// =============================================================

package main

import "fmt"

type TreeNode struct { Val int; Left, Right *TreeNode }

func preorderTraversal(root *TreeNode) []int {
    if root == nil { return []int{} }
    out := []int{}; st := []*TreeNode{root}
    for len(st) > 0 {
        n := st[len(st)-1]; st = st[:len(st)-1]
        out = append(out, n.Val)
        if n.Right != nil { st = append(st, n.Right) }
        if n.Left  != nil { st = append(st, n.Left) }
    }
    return out
}

func main() {
    r := &TreeNode{Val:1, Right:&TreeNode{Val:2, Left:&TreeNode{Val:3}}}
    fmt.Println(preorderTraversal(r))
}
