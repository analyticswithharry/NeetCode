//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 226 -- Combination Sum IV
// Category   : 1-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 113
// =============================================================
//
// QUESTION:
//   Count ordered combinations of nums summing to target.
// =============================================================
package main
import "fmt"
func combSum4(nums []int, t int) int { dp:=make([]int,t+1); dp[0]=1; for v:=1;v<=t;v++ { for _,x:=range nums { if v>=x { dp[v]+=dp[v-x] } } }; return dp[t] }
func main(){ fmt.Println(combSum4([]int{1,2,3},4)) }
