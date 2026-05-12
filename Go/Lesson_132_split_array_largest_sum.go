//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 132 -- Split Array Largest Sum
// Category   : Binary Search
// Difficulty : Hard
// Study Plan : Day 66
// =============================================================
//
// QUESTION:
//   Split nums into k non-empty contiguous parts to minimize the largest sum among parts.
// =============================================================
package main
import "fmt"
func split(a []int,k int) int { can:=func(mx int) bool { c,s:=1,0; for _,x:=range a { if s+x>mx { c++; s=x } else { s+=x } }; return c<=k }; lo,hi:=a[0],0; for _,x:=range a { if x>lo { lo=x }; hi+=x }; for lo<hi { m:=(lo+hi)/2; if can(m) { hi=m } else { lo=m+1 } }; return lo }
func main(){ fmt.Println(split([]int{7,2,5,10,8},2)) }
