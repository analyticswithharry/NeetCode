//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 115 -- Plus One
// Category   : Math and Geometry
// Difficulty : Easy
// Study Plan : Day 58
// =============================================================
//
// QUESTION:
//   Given a non-empty array of decimal digits representing a non-negative integer, add one and return the resulting array.
// =============================================================
package main
import "fmt"
func plusOne(d []int) []int { d=append([]int{},d...); for i:=len(d)-1;i>=0;i-- { if d[i]<9 { d[i]++; return d }; d[i]=0 }; return append([]int{1},d...) }
func main(){ fmt.Println(plusOne([]int{1,2,3})); fmt.Println(plusOne([]int{9,9})) }
