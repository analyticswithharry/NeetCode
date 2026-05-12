//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 111 -- Single Number
// Category   : Bit Manipulation
// Difficulty : Easy
// Study Plan : Day 56
// =============================================================
//
// QUESTION:
//   Given a non-empty array of integers, every element appears twice except for one. Find that single one. O(1) extra space.
// =============================================================
package main
import "fmt"
func single(a []int) int { r:=0; for _,x:=range a { r^=x }; return r }
func main(){ fmt.Println(single([]int{2,2,1})); fmt.Println(single([]int{4,1,2,1,2})) }
