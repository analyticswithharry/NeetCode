//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 005 -- Binary Tree Inorder Traversal
// Category   : Trees
// Difficulty : Easy
// Study Plan : Day 3
// =============================================================
//
// QUESTION:
//   Given the root of a binary tree, return the inorder (Left, Root, Right)
//   traversal of its nodes' values.
//
//   Example:
//     Input : root = [1,null,2,3]
//     Output: [1, 3, 2]
// =============================================================

package main

import "fmt"

type TreeNode struct { Val int; Left, Right *TreeNode }

func inorderTraversal(root *TreeNode) []int {
    out := []int{}; st := []*TreeNode{}; cur := root
    for cur != nil || len(st) > 0 {
        for cur != nil { st = append(st, cur); cur = cur.Left }
        n := len(st) - 1; cur = st[n]; st = st[:n]
        out = append(out, cur.Val); cur = cur.Right
    }
    return out
}

func main() {
    r := &TreeNode{Val:1, Right:&TreeNode{Val:2, Left:&TreeNode{Val:3}}}
    fmt.Println(inorderTraversal(r))
}
