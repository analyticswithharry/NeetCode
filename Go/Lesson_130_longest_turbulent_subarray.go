//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 130 -- Longest Turbulent Subarray
// Category   : Greedy
// Difficulty : Medium
// Study Plan : Day 65
// =============================================================
//
// QUESTION:
//   Given an array, return length of longest turbulent subarray (alternating > <).
// =============================================================
package main
import "fmt"
func turb(a []int) int { inc,dec,b:=1,1,1; for i:=1;i<len(a);i++ { if a[i]>a[i-1] { inc=dec+1; dec=1 } else if a[i]<a[i-1] { dec=inc+1; inc=1 } else { inc=1; dec=1 }; m:=inc; if dec>m { m=dec }; if m>b { b=m } }; return b }
func main(){ fmt.Println(turb([]int{9,4,2,10,7,8,8,1,9})) }
