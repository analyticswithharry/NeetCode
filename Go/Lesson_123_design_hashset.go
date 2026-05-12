//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 123 -- Design HashSet
// Category   : Arrays and Hashing
// Difficulty : Easy
// Study Plan : Day 62
// =============================================================
//
// QUESTION:
//   Design a HashSet (without built-in set): add, remove, contains.
// =============================================================
package main
import "fmt"
type MyHashSet struct{ b [769][]int }
func (s *MyHashSet) h(k int) int { return ((k%769)+769)%769 }
func (s *MyHashSet) Add(k int){ i:=s.h(k); for _,x:=range s.b[i]{ if x==k{ return } }; s.b[i]=append(s.b[i],k) }
func (s *MyHashSet) Remove(k int){ i:=s.h(k); for j,x:=range s.b[i]{ if x==k{ s.b[i]=append(s.b[i][:j],s.b[i][j+1:]...); return } } }
func (s *MyHashSet) Contains(k int) bool { i:=s.h(k); for _,x:=range s.b[i]{ if x==k{ return true } }; return false }
func main(){ s:=&MyHashSet{}; s.Add(1); s.Add(2); fmt.Println(s.Contains(1), s.Contains(3)); s.Remove(2); fmt.Println(s.Contains(2)) }
