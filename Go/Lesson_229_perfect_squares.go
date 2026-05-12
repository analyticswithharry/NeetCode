//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 229 -- Perfect Squares
// Category   : 1-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 115
// =============================================================
//
// QUESTION:
//   Min number of perfect-square numbers summing to n.
// =============================================================
package main
import "fmt"
func numSquares(n int) int { dp:=make([]int,n+1); for i:=1;i<=n;i++ { dp[i]=1<<30; for j:=1;j*j<=i;j++ { if dp[i-j*j]+1<dp[i] { dp[i]=dp[i-j*j]+1 } } }; return dp[n] }
func main(){ fmt.Println(numSquares(12)) }
