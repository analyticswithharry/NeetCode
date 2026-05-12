//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 129 -- Maximum Sum Circular Subarray
// Category   : Greedy
// Difficulty : Medium
// Study Plan : Day 65
// =============================================================
//
// QUESTION:
//   Given a circular integer array, find the maximum subarray sum (subarray may wrap).
// =============================================================
package main
import "fmt"
func maxCirc(a []int) int { tot,mxc,cur,mnc,c2:=0,a[0],a[0],a[0],a[0]; for i,x:=range a { if i>0 { if x>cur+x { cur=x } else { cur+=x }; if cur>mxc { mxc=cur }; if x<c2+x { c2=x } else { c2+=x }; if c2<mnc { mnc=c2 } }; tot+=x }; if mxc<0 { return mxc }; if mxc>tot-mnc { return mxc }; return tot-mnc }
func main(){ fmt.Println(maxCirc([]int{1,-2,3,-2})); fmt.Println(maxCirc([]int{5,-3,5})); fmt.Println(maxCirc([]int{-3,-2,-3})) }
