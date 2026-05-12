//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 237 -- Longest Consecutive Sequence
// Category   : Arrays and Hashing
// Difficulty : Medium
// Study Plan : Day 119
// =============================================================
//
// QUESTION:
//   Length of longest run of consecutive integers in unsorted array. O(n) hashset.
// =============================================================
package main
import "fmt"
func longestConsec(n []int) int { s:=map[int]bool{}; for _,x:=range n{s[x]=true}; best:=0; for x:=range s { if !s[x-1] { y:=x; for s[y+1]{y++}; if y-x+1>best{best=y-x+1} } }; return best }
func main(){ fmt.Println(longestConsec([]int{100,4,200,1,3,2})) }
