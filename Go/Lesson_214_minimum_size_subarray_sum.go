//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 214 -- Minimum Size Subarray Sum
// Category   : Sliding Window
// Difficulty : Medium
// Study Plan : Day 107
// =============================================================
//
// QUESTION:
//   Return the minimum length of a contiguous subarray whose sum is >= target. 0 if none.
// =============================================================
package main
import "fmt"
func minSubArrayLen(t int, n []int) int { l,s,ans:=0,0,1<<30; for r:=0;r<len(n);r++ { s+=n[r]; for s>=t { if r-l+1<ans { ans=r-l+1 }; s-=n[l]; l++ } }; if ans==1<<30 { return 0 }; return ans }
func main(){ fmt.Println(minSubArrayLen(7,[]int{2,3,1,2,4,3})) }
