//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 112 -- Sum of Two Integers
// Category   : Bit Manipulation
// Difficulty : Medium
// Study Plan : Day 56
// =============================================================
//
// QUESTION:
//   Given two integers a and b, return the sum without using + or -.
// =============================================================
package main
import "fmt"
func add(a,b int) int { for b!=0 { c:=(a&b)<<1; a=a^b; b=c }; return a }
func main(){ fmt.Println(add(1,2)); fmt.Println(add(-2,3)) }
