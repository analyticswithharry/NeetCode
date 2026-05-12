//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 230 -- Integer Break
// Category   : 1-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 115
// =============================================================
//
// QUESTION:
//   Break n into >=2 positive ints; maximize product.
// =============================================================
package main
import "fmt"
func integerBreak(n int) int { dp:=make([]int,n+1); dp[1]=1; for i:=2;i<=n;i++ { for j:=1;j<i;j++ { m:=i-j; if dp[i-j]>m { m=dp[i-j] }; if j*m>dp[i] { dp[i]=j*m } } }; return dp[n] }
func main(){ fmt.Println(integerBreak(10)) }
