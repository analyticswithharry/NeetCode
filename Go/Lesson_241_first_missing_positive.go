//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 241 -- First Missing Positive
// Category   : Arrays and Hashing
// Difficulty : Hard
// Study Plan : Day 121
// =============================================================
//
// QUESTION:
//   Smallest missing positive int. O(n) time, O(1) extra space (cyclic placement).
// =============================================================
package main
import "fmt"
func firstMissing(n []int) int { N:=len(n); for i:=0;i<N;i++ { for n[i]>=1&&n[i]<=N&&n[n[i]-1]!=n[i] { j:=n[i]-1; n[i],n[j]=n[j],n[i] } }; for i:=0;i<N;i++ { if n[i]!=i+1 { return i+1 } }; return N+1 }
func main(){ fmt.Println(firstMissing([]int{3,4,-1,1})) }
