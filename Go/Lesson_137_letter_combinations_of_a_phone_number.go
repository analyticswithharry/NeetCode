//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 137 -- Letter Combinations of a Phone Number
// Category   : Backtracking
// Difficulty : Medium
// Study Plan : Day 69
// =============================================================
//
// QUESTION:
//   Given digits 2-9, return all possible letter combinations the number could represent.
// =============================================================
package main
import "fmt"
func letters(d string) []string { if d=="" { return nil }; m:=[]string{"","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"}; r:=[]string{""}; for _,c:=range d { var n []string; for _,p:=range r { for _,x:=range m[c-'0'] { n=append(n,p+string(x)) } }; r=n }; return r }
func main(){ fmt.Println(letters("23")) }
