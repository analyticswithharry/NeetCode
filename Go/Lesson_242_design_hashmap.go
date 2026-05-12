//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 242 -- Design HashMap
// Category   : Arrays and Hashing
// Difficulty : Easy
// Study Plan : Day 121
// =============================================================
//
// QUESTION:
//   Implement HashMap with put/get/remove using bucket separate chaining.
// =============================================================
package main
import "fmt"
type HM struct{ b [][]int }
func New() *HM { return &HM{b:make([][]int,997)} }
func (h *HM) idx(k int) int { return ((k%997)+997)%997 }
func (h *HM) Put(k,v int){ i:=h.idx(k); for j:=0;j<len(h.b[i]);j+=2 { if h.b[i][j]==k { h.b[i][j+1]=v; return } }; h.b[i]=append(h.b[i],k,v) }
func (h *HM) Get(k int) int { i:=h.idx(k); for j:=0;j<len(h.b[i]);j+=2 { if h.b[i][j]==k { return h.b[i][j+1] } }; return -1 }
func (h *HM) Remove(k int){ i:=h.idx(k); for j:=0;j<len(h.b[i]);j+=2 { if h.b[i][j]==k { h.b[i]=append(h.b[i][:j],h.b[i][j+2:]...); return } } }
func main(){ m:=New(); m.Put(1,1); m.Put(2,2); fmt.Println(m.Get(1),m.Get(3)); m.Remove(1); fmt.Println(m.Get(1)) }
