//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 126 -- Container With Most Water
// Category   : Two Pointers
// Difficulty : Medium
// Study Plan : Day 63
// =============================================================
//
// QUESTION:
//   Given heights, find two lines that form the container holding most water.
// =============================================================
package main
import "fmt"
func maxArea(h []int) int { l,r:=0,len(h)-1; b:=0; for l<r { x:=(r-l); m:=h[l]; if h[r]<m { m=h[r] }; if x*m>b { b=x*m }; if h[l]<h[r] { l++ } else { r-- } }; return b }
func main(){ fmt.Println(maxArea([]int{1,8,6,2,5,4,8,3,7})) }
