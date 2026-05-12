//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 080 -- Binary Tree Level Order Traversal
// Category   : Trees
// Difficulty : Medium
// Study Plan : Day 40
// =============================================================
//
// QUESTION:
//   Return level-order traversal of a binary tree as list of lists.
//
//   Example: [3,9,20,null,null,15,7] -> [[3],[9,20],[15,7]]
// =============================================================

package main
import "fmt"
type TreeNode struct { Val int; Left, Right *TreeNode }
func levelOrder(root *TreeNode) [][]int {
    out := [][]int{}; if root == nil { return out }
    q := []*TreeNode{root}
    for len(q) > 0 {
        n := len(q); lvl := []int{}
        for i := 0; i < n; i++ { x := q[0]; q = q[1:]; lvl = append(lvl, x.Val)
            if x.Left != nil { q = append(q, x.Left) }
            if x.Right != nil { q = append(q, x.Right) } }
        out = append(out, lvl)
    }
    return out
}
func main(){
    r := &TreeNode{Val:3, Left:&TreeNode{Val:9}, Right:&TreeNode{Val:20, Left:&TreeNode{Val:15}, Right:&TreeNode{Val:7}}}
    fmt.Println(levelOrder(r))
}
