//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 247 -- Remove Duplicates From Sorted Array
// Category   : Two Pointers
// Difficulty : Easy
// Study Plan : Day 124
// =============================================================
//
// QUESTION:
//   In-place dedupe of sorted array. Return new length.
// =============================================================
package main
import "fmt"
func dedupe(a []int) int { if len(a)==0 { return 0 }; k:=1; for i:=1;i<len(a);i++ { if a[i]!=a[k-1] { a[k]=a[i]; k++ } }; return k }
func main(){ a:=[]int{1,1,2,2,3}; n:=dedupe(a); fmt.Println(n,a[:n]) }
