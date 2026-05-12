//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 143 -- Palindromic Substrings
// Category   : 1-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 72
// =============================================================
//
// QUESTION:
//   Count number of palindromic substrings in s.
// =============================================================
package main
import "fmt"
func count(s string) int { c:=0; ex:=func(a,b int){ for a>=0 && b<len(s) && s[a]==s[b] { c++; a--; b++ } }; for i:=0;i<len(s);i++ { ex(i,i); ex(i,i+1) }; return c }
func main(){ fmt.Println(count("abc")); fmt.Println(count("aaa")) }
