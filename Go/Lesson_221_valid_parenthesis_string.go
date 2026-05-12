//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 221 -- Valid Parenthesis String
// Category   : Greedy
// Difficulty : Medium
// Study Plan : Day 111
// =============================================================
//
// QUESTION:
//   '*' can be '(' ')' or empty. Determine if string can be valid.
// =============================================================
package main
import "fmt"
func checkValid(s string) bool { lo,hi:=0,0; for _,c:=range s { if c=='(' { lo++ } else { lo-- }; if c!=')' { hi++ } else { hi-- }; if hi<0 { return false }; if lo<0 { lo=0 } }; return lo==0 }
func main(){ fmt.Println(checkValid("(*))")) }
