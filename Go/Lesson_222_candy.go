//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 222 -- Candy
// Category   : Greedy
// Difficulty : Hard
// Study Plan : Day 111
// =============================================================
//
// QUESTION:
//   Each child gets >=1 candy; higher rating gets more than neighbors. Return min candies.
// =============================================================
package main
import "fmt"
func candy(r []int) int { n:=len(r); a:=make([]int,n); for i:=range a{a[i]=1}; for i:=1;i<n;i++ { if r[i]>r[i-1] { a[i]=a[i-1]+1 } }; for i:=n-2;i>=0;i-- { if r[i]>r[i+1] && a[i]<=a[i+1] { a[i]=a[i+1]+1 } }; s:=0; for _,x:=range a { s+=x }; return s }
func main(){ fmt.Println(candy([]int{1,0,2})) }
