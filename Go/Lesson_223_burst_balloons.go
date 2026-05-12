//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 223 -- Burst Balloons
// Category   : 2-D Dynamic Programming
// Difficulty : Hard
// Study Plan : Day 112
// =============================================================
//
// QUESTION:
//   Burst balloons; coins = nums[l]*nums[i]*nums[r]. Maximize total.
// =============================================================
package main
import "fmt"
func maxCoins(nums []int) int { a:=append([]int{1},nums...); a=append(a,1); n:=len(a); dp:=make([][]int,n); for i:=range dp{dp[i]=make([]int,n)}; for L:=2;L<n;L++ { for l:=0;l+L<n;l++ { r:=l+L; for i:=l+1;i<r;i++ { v:=dp[l][i]+dp[i][r]+a[l]*a[i]*a[r]; if v>dp[l][r]{dp[l][r]=v} } } }; return dp[0][n-1] }
func main(){ fmt.Println(maxCoins([]int{3,1,5,8})) }
