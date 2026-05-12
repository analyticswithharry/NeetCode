//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 246 -- Largest Rectangle In Histogram
// Category   : Stack
// Difficulty : Hard
// Study Plan : Day 123
// =============================================================
//
// QUESTION:
//   Max rectangular area in histogram. Monotonic stack.
// =============================================================
package main
import "fmt"
func largestRect(h []int) int { h=append(h,0); st:=[]int{}; best:=0; for i:=0;i<len(h);i++ { for len(st)>0 && h[st[len(st)-1]]>h[i] { top:=st[len(st)-1]; st=st[:len(st)-1]; w:=i; if len(st)>0 { w=i-st[len(st)-1]-1 }; if h[top]*w>best { best=h[top]*w } }; st=append(st,i) }; return best }
func main(){ fmt.Println(largestRect([]int{2,1,5,6,2,3})) }
