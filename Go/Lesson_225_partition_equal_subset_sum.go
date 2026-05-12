//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 225 -- Partition Equal Subset Sum
// Category   : 1-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 113
// =============================================================
//
// QUESTION:
//   Can the array be split into two equal-sum subsets? Subset-sum DP.
// =============================================================
package main
import "fmt"
func canPartition(nums []int) bool { s:=0; for _,x:=range nums{s+=x}; if s%2==1 { return false }; t:=s/2; dp:=make([]bool,t+1); dp[0]=true; for _,x:=range nums { for v:=t;v>=x;v-- { dp[v]=dp[v]||dp[v-x] } }; return dp[t] }
func main(){ fmt.Println(canPartition([]int{1,5,11,5})) }
