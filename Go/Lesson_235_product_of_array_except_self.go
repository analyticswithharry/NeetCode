//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 235 -- Product of Array Except Self
// Category   : Arrays and Hashing
// Difficulty : Medium
// Study Plan : Day 118
// =============================================================
//
// QUESTION:
//   Return array where output[i] = product of all nums except nums[i]. O(n) no division.
// =============================================================
package main
import "fmt"
func productExceptSelf(n []int) []int { o:=make([]int,len(n)); p:=1; for i:=0;i<len(n);i++ { o[i]=p; p*=n[i] }; p=1; for i:=len(n)-1;i>=0;i-- { o[i]*=p; p*=n[i] }; return o }
func main(){ fmt.Println(productExceptSelf([]int{1,2,3,4})) }
