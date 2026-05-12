//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 125 -- Merge Sorted Array
// Category   : Two Pointers
// Difficulty : Easy
// Study Plan : Day 63
// =============================================================
//
// QUESTION:
//   Given nums1 (length m+n) and nums2 (length n) sorted, merge nums2 into nums1 in-place sorted.
// =============================================================
package main
import "fmt"
func merge(a []int,m int,b []int,n int) []int { i,j,k:=m-1,n-1,m+n-1; for j>=0 { if i>=0 && a[i]>b[j] { a[k]=a[i]; i-- } else { a[k]=b[j]; j-- }; k-- }; return a }
func main(){ fmt.Println(merge([]int{1,2,3,0,0,0},3,[]int{2,5,6},3)) }
