//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 248 -- Detect Squares
// Category   : Math and Geometry
// Difficulty : Medium
// Study Plan : Day 124
// =============================================================
//
// QUESTION:
//   Add point or count axis-aligned squares with given query point.
// =============================================================
package main
import "fmt"
type pt struct{x,y int}
type DS struct{c map[pt]int}
func New() *DS{return &DS{map[pt]int{}}}
func (s *DS) Add(p pt){ s.c[p]++ }
func (s *DS) Count(p pt) int { tot:=0; for k,v:=range s.c { if k.x==p.x { continue }; if abs(k.x-p.x)!=abs(k.y-p.y) { continue }; tot+=v*s.c[pt{k.x,p.y}]*s.c[pt{p.x,k.y}] }; return tot }
func abs(x int) int { if x<0 {return -x}; return x }
func main(){ d:=New(); for _,p:=range []pt{{3,10},{11,2},{3,2}}{ d.Add(p) }; fmt.Println(d.Count(pt{11,10})) }
