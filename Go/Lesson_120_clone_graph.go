//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 120 -- Clone Graph
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 60
// =============================================================
//
// QUESTION:
//   Given a node in a connected undirected graph, return a deep copy of the graph.
// =============================================================
package main
import "fmt"
type Node struct{ Val int; Neighbors []*Node }
func clone(n *Node, seen map[*Node]*Node) *Node { if n==nil { return nil }; if c,ok:=seen[n]; ok { return c }; c:=&Node{Val:n.Val}; seen[n]=c; for _,y:=range n.Neighbors { c.Neighbors=append(c.Neighbors,clone(y,seen)) }; return c }
func main(){ a:=&Node{Val:1}; b:=&Node{Val:2}; a.Neighbors=[]*Node{b}; b.Neighbors=[]*Node{a}; c:=clone(a,map[*Node]*Node{}); fmt.Println(c.Val, c.Neighbors[0].Val, c.Neighbors[0].Neighbors[0].Val) }
