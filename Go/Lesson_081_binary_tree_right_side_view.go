//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 081 -- Binary Tree Right Side View
// Category   : Trees
// Difficulty : Medium
// Study Plan : Day 41
// =============================================================
//
// QUESTION:
//   Return the values of nodes you'd see ordered from top to bottom from the right side.
//
//   Example: [1,2,3,null,5,null,4] -> [1,3,4]
// =============================================================

package main
import "fmt"
type TreeNode struct { Val int; Left, Right *TreeNode }
func rightSideView(root *TreeNode) []int {
    out := []int{}; if root == nil { return out }
    q := []*TreeNode{root}
    for len(q) > 0 {
        n := len(q)
        for i := 0; i < n; i++ { x := q[0]; q = q[1:]; if i == n-1 { out = append(out, x.Val) }
            if x.Left != nil { q = append(q, x.Left) }
            if x.Right != nil { q = append(q, x.Right) } }
    }
    return out
}
func main(){
    r := &TreeNode{Val:1, Left:&TreeNode{Val:2, Right:&TreeNode{Val:5}}, Right:&TreeNode{Val:3, Right:&TreeNode{Val:4}}}
    fmt.Println(rightSideView(r))
}
