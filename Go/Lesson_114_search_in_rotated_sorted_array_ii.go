//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 114 -- Search In Rotated Sorted Array II
// Category   : Binary Search
// Difficulty : Medium
// Study Plan : Day 57
// =============================================================
//
// QUESTION:
//   Rotated sorted array may contain duplicates. Return true if target exists.
// =============================================================
package main
import "fmt"
func search(a []int,t int) bool { lo,hi:=0,len(a)-1; for lo<=hi { m:=(lo+hi)/2; if a[m]==t { return true }; if a[lo]==a[m] && a[m]==a[hi] { lo++; hi-- } else if a[lo]<=a[m] { if a[lo]<=t && t<a[m] { hi=m-1 } else { lo=m+1 } } else { if a[m]<t && t<=a[hi] { lo=m+1 } else { hi=m-1 } } }; return false }
func main(){ a:=[]int{2,5,6,0,0,1,2}; fmt.Println(search(a,0)); fmt.Println(search(a,3)) }
