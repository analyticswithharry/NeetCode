//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 158 -- Minimum Array End
// Category   : Bit Manipulation
// Difficulty : Medium
// Study Plan : Day 79
// =============================================================
//
// QUESTION:
//   Given n and x, return min possible value v such that AND of n distinct integers (>=x, <=v, all sharing bits of x) equals x. Equivalent: spread (n-1) over the zero-bits of x.
// =============================================================
package main
import "fmt"
func minEnd(n,x int64) int64 { n--; r:=x; var bit,nb int64=1,1; for nb<=n { if x&bit==0 { if n&nb!=0 { r|=bit }; nb<<=1 }; bit<<=1 }; return r }
func main(){ fmt.Println(minEnd(3,4)); fmt.Println(minEnd(2,7)) }
