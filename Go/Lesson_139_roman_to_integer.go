//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 139 -- Roman to Integer
// Category   : Math and Geometry
// Difficulty : Easy
// Study Plan : Day 70
// =============================================================
//
// QUESTION:
//   Convert Roman numeral string to integer.
// =============================================================
package main
import "fmt"
func r2i(s string) int { m:=map[byte]int{'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}; t,p:=0,0; for i:=len(s)-1;i>=0;i-- { v:=m[s[i]]; if v<p { t-=v } else { t+=v; p=v } }; return t }
func main(){ fmt.Println(r2i("III")); fmt.Println(r2i("LVIII")); fmt.Println(r2i("MCMXCIV")) }
