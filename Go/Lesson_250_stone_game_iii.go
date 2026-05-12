//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 250 -- Stone Game III
// Category   : 1-D Dynamic Programming
// Difficulty : Hard
// Study Plan : Day 125
// =============================================================
//
// QUESTION:
//   Players take 1-3 stones from front; maximize own score. Return Alice/Bob/Tie.
// =============================================================
package main
import "fmt"
func stoneGameIII(s []int) string { n:=len(s); dp:=make([]int,n+1); for i:=n-1;i>=0;i-- { best:=-1<<30; take:=0; for k:=0;k<3 && i+k<n;k++ { take+=s[i+k]; if take-dp[i+k+1]>best { best=take-dp[i+k+1] } }; dp[i]=best }; if dp[0]>0 { return "Alice" }; if dp[0]<0 { return "Bob" }; return "Tie" }
func main(){ fmt.Println(stoneGameIII([]int{1,2,3,7})) }
