//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 147 -- Last Stone Weight II
// Category   : 2-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 74
// =============================================================
//
// QUESTION:
//   Given stones, smash to minimize remaining weight (subset partition).
// =============================================================
package main
import "fmt"
func lsw2(s []int) int { t:=0; for _,x:=range s { t+=x }; cap:=t/2; dp:=make([]bool,cap+1); dp[0]=true; for _,x:=range s { for j:=cap;j>=x;j-- { if dp[j-x] { dp[j]=true } } }; for j:=cap;j>=0;j-- { if dp[j] { return t-2*j } }; return 0 }
func main(){ fmt.Println(lsw2([]int{2,7,4,1,8,1})); fmt.Println(lsw2([]int{31,26,33,21,40})) }
