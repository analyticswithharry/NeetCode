//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 148 -- Best Time to Buy And Sell Stock With Cooldown
// Category   : 2-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 74
// =============================================================
//
// QUESTION:
//   Stock prices; can do unlimited transactions but after selling must cooldown 1 day. Max profit.
// =============================================================
package main
import "fmt"
func maxP(p []int) int { hold:=-p[0]; sold:=0; rest:=0; for i:=1;i<len(p);i++ { h:=hold; if rest-p[i]>h { h=rest-p[i] }; s:=hold+p[i]; r:=rest; if sold>r { r=sold }; hold=h; sold=s; rest=r }; if sold>rest { return sold }; return rest }
func main(){ fmt.Println(maxP([]int{1,2,3,0,2})) }
