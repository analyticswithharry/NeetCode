//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 238 -- Best Time to Buy And Sell Stock II
// Category   : Arrays and Hashing
// Difficulty : Medium
// Study Plan : Day 119
// =============================================================
//
// QUESTION:
//   Multiple transactions allowed. Sum positive deltas.
// =============================================================
package main
import "fmt"
func maxProfit(p []int) int { s:=0; for i:=1;i<len(p);i++ { if p[i]>p[i-1]{ s+=p[i]-p[i-1] } }; return s }
func main(){ fmt.Println(maxProfit([]int{7,1,5,3,6,4})) }
