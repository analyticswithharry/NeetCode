//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 245 -- Sliding Window Maximum
// Category   : Sliding Window
// Difficulty : Hard
// Study Plan : Day 123
// =============================================================
//
// QUESTION:
//   Max in each window of size k. Monotonic deque.
// =============================================================
package main
import "fmt"
func maxSliding(n []int, k int) []int { dq:=[]int{}; out:=[]int{}; for i,x:=range n { for len(dq)>0 && n[dq[len(dq)-1]]<=x { dq=dq[:len(dq)-1] }; dq=append(dq,i); if dq[0]<=i-k { dq=dq[1:] }; if i>=k-1 { out=append(out,n[dq[0]]) } }; return out }
func main(){ fmt.Println(maxSliding([]int{1,3,-1,-3,5,3,6,7},3)) }
