//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 128 -- Reverse Integer
// Category   : Bit Manipulation
// Difficulty : Medium
// Study Plan : Day 64
// =============================================================
//
// QUESTION:
//   Reverse digits of a signed 32-bit integer; return 0 on overflow.
// =============================================================
package main
import "fmt"
func rev(x int) int { r:=0; for x!=0 { r=r*10+x%10; x/=10 }; if r<-(1<<31) || r>(1<<31)-1 { return 0 }; return r }
func main(){ fmt.Println(rev(123)); fmt.Println(rev(-456)); fmt.Println(rev(1534236469)) }
