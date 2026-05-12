//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 150 -- Online Stock Span
// Category   : Stack
// Difficulty : Medium
// Study Plan : Day 75
// =============================================================
//
// QUESTION:
//   Implement StockSpanner.next(price): consecutive days <= today's price (including today).
// =============================================================
package main
import "fmt"
type Pr struct{ P,S int }
type StockSpanner struct{ st []Pr }
func (s *StockSpanner) Next(p int) int { v:=1; for len(s.st)>0 && s.st[len(s.st)-1].P<=p { v+=s.st[len(s.st)-1].S; s.st=s.st[:len(s.st)-1] }; s.st=append(s.st,Pr{p,v}); return v }
func main(){ s:=&StockSpanner{}; for _,v:=range []int{100,80,60,70,60,75,85} { fmt.Print(s.Next(v)," ") }; fmt.Println() }
