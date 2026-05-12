//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 240 -- Subarray Sum Equals K
// Category   : Arrays and Hashing
// Difficulty : Medium
// Study Plan : Day 120
// =============================================================
//
// QUESTION:
//   Count subarrays with sum k using prefix-sum frequency map.
// =============================================================
package main
import "fmt"
func subarraySum(n []int, k int) int { m:=map[int]int{0:1}; s,c:=0,0; for _,x:=range n { s+=x; c+=m[s-k]; m[s]++ }; return c }
func main(){ fmt.Println(subarraySum([]int{1,1,1},2)) }
