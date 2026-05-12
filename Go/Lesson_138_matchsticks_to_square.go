//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 138 -- Matchsticks to Square
// Category   : Backtracking
// Difficulty : Medium
// Study Plan : Day 69
// =============================================================
//
// QUESTION:
//   Use all matchsticks to form a square. Return true if possible.
// =============================================================
package main
import ("fmt";"sort")
func square(m []int) bool { s:=0; for _,x:=range m { s+=x }; if s%4!=0 { return false }; side:=s/4; sort.Sort(sort.Reverse(sort.IntSlice(m))); if m[0]>side { return false }; sides:=[4]int{}; var rec func(i int) bool; rec=func(i int) bool { if i==len(m) { return sides[0]==side && sides[1]==side && sides[2]==side }; for j:=0;j<4;j++ { if sides[j]+m[i]>side { continue }; if j>0 && sides[j]==sides[j-1] { continue }; sides[j]+=m[i]; if rec(i+1) { return true }; sides[j]-=m[i] }; return false }; return rec(0) }
func main(){ fmt.Println(square([]int{1,1,2,2,2})); fmt.Println(square([]int{3,3,3,3,4})) }
