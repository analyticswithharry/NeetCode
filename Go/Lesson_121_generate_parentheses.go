//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 121 -- Generate Parentheses
// Category   : Stack
// Difficulty : Medium
// Study Plan : Day 61
// =============================================================
//
// QUESTION:
//   Given n pairs of parentheses, generate all combinations of well-formed parentheses.
// =============================================================
package main
import "fmt"
func gen(n int) []string { var r []string; var rec func(s string,o,c int); rec=func(s string,o,c int){ if len(s)==2*n { r=append(r,s); return }; if o<n { rec(s+"(",o+1,c) }; if c<o { rec(s+")",o,c+1) } }; rec("",0,0); return r }
func main(){ fmt.Println(gen(3)) }
