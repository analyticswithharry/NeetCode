//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 082 -- Count Good Nodes in Binary Tree
// Category   : Trees
// Difficulty : Medium
// Study Plan : Day 41
// =============================================================
//
// QUESTION:
//   A node X is good if no node on the path from root to X has value greater than X. Count good nodes.
//
//   Example: [3,1,4,3,null,1,5] -> 4
// =============================================================

package main
import "fmt"
type TreeNode struct { Val int; Left, Right *TreeNode }
func goodNodes(root *TreeNode) int {
    var dfs func(n *TreeNode, mx int) int
    dfs = func(n *TreeNode, mx int) int {
        if n == nil { return 0 }
        c := 0; if n.Val >= mx { c = 1 }
        m := mx; if n.Val > m { m = n.Val }
        return c + dfs(n.Left, m) + dfs(n.Right, m)
    }
    return dfs(root, root.Val)
}
func main(){
    r := &TreeNode{Val:3, Left:&TreeNode{Val:1, Left:&TreeNode{Val:3}}, Right:&TreeNode{Val:4, Left:&TreeNode{Val:1}, Right:&TreeNode{Val:5}}}
    fmt.Println(goodNodes(r))
}
