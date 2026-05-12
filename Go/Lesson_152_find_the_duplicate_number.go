//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 152 -- Find The Duplicate Number
// Category   : Linked List
// Difficulty : Medium
// Study Plan : Day 76
// =============================================================
//
// QUESTION:
//   Array length n+1 with values in [1,n] containing one duplicate. Find it. O(1) extra space.
// =============================================================
package main
import "fmt"
func dup(a []int) int { s:=a[0]; f:=a[0]; for { s=a[s]; f=a[a[f]]; if s==f { break } }; s=a[0]; for s!=f { s=a[s]; f=a[f] }; return s }
func main(){ fmt.Println(dup([]int{1,3,4,2,2})); fmt.Println(dup([]int{3,1,3,4,2})) }
