//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 151 -- Add Two Numbers
// Category   : Linked List
// Difficulty : Medium
// Study Plan : Day 76
// =============================================================
//
// QUESTION:
//   Two non-empty linked lists (least-significant-digit first). Add and return sum as linked list.
// =============================================================
package main
import "fmt"
type LN struct{ Val int; Next *LN }
func add(a,b *LN) *LN { d:=&LN{}; cur:=d; c:=0; for a!=nil || b!=nil || c!=0 { v:=c; if a!=nil { v+=a.Val; a=a.Next }; if b!=nil { v+=b.Val; b=b.Next }; c=v/10; cur.Next=&LN{Val:v%10}; cur=cur.Next }; return d.Next }
func fromArr(x []int) *LN { d:=&LN{}; c:=d; for _,v:=range x { c.Next=&LN{Val:v}; c=c.Next }; return d.Next }
func main(){ r:=add(fromArr([]int{2,4,3}),fromArr([]int{5,6,4})); for r!=nil { fmt.Print(r.Val," "); r=r.Next }; fmt.Println() }
