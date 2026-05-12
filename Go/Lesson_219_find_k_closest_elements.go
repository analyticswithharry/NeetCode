//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 219 -- Find K Closest Elements
// Category   : Sliding Window
// Difficulty : Medium
// Study Plan : Day 110
// =============================================================
//
// QUESTION:
//   Return k closest sorted ints to x (binary search the window).
// =============================================================
package main
import "fmt"
func findClosest(a []int, k,x int) []int { l,r:=0,len(a)-k; for l<r { m:=(l+r)/2; if x-a[m]>a[m+k]-x { l=m+1 } else { r=m } }; return a[l:l+k] }
func main(){ fmt.Println(findClosest([]int{1,2,3,4,5},4,3)) }
