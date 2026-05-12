//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 133 -- Counting Bits
// Category   : Bit Manipulation
// Difficulty : Easy
// Study Plan : Day 67
// =============================================================
//
// QUESTION:
//   For 0..n return array where ans[i] = number of 1-bits in i.
// =============================================================
package main
import "fmt"
func cb(n int) []int { a:=make([]int,n+1); for i:=1;i<=n;i++ { a[i]=a[i>>1]+(i&1) }; return a }
func main(){ fmt.Println(cb(5)) }
