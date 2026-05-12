//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 136 -- Car Pooling
// Category   : Heap Priority Queue
// Difficulty : Medium
// Study Plan : Day 68
// =============================================================
//
// QUESTION:
//   Trips [numPassengers,from,to]; capacity. Return true iff possible to pick up & drop off all passengers without exceeding capacity.
// =============================================================
package main
import "fmt"
func carPool(t [][]int,cap int) bool { e:=make([]int,1001); for _,x:=range t { e[x[1]]+=x[0]; e[x[2]]-=x[0] }; s:=0; for _,v:=range e { s+=v; if s>cap { return false } }; return true }
func main(){ fmt.Println(carPool([][]int{{2,1,5},{3,3,7}},4)); fmt.Println(carPool([][]int{{2,1,5},{3,3,7}},5)) }
