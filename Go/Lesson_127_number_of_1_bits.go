//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 127 -- Number of 1 Bits
// Category   : Bit Manipulation
// Difficulty : Easy
// Study Plan : Day 64
// =============================================================
//
// QUESTION:
//   Return the number of 1 bits in unsigned int.
// =============================================================
package main
import "fmt"
func hw(n uint) int { c:=0; for n!=0 { n &= n-1; c++ }; return c }
func main(){ fmt.Println(hw(11)); fmt.Println(hw(128)) }
