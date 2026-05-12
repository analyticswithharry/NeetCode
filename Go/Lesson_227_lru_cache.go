//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 227 -- LRU Cache
// Category   : Linked List
// Difficulty : Medium
// Study Plan : Day 114
// =============================================================
//
// QUESTION:
//   Design LRU cache with O(1) get and put.
// =============================================================
package main
import ("container/list";"fmt")
type LRU struct{c int; l *list.List; m map[int]*list.Element}
type kv struct{k,v int}
func New(c int) *LRU { return &LRU{c,list.New(),map[int]*list.Element{}} }
func (s *LRU) Get(k int) int { if e,ok:=s.m[k]; ok { s.l.MoveToFront(e); return e.Value.(*kv).v }; return -1 }
func (s *LRU) Put(k,v int){ if e,ok:=s.m[k]; ok { e.Value.(*kv).v=v; s.l.MoveToFront(e); return }; e:=s.l.PushFront(&kv{k,v}); s.m[k]=e; if s.l.Len()>s.c { b:=s.l.Back(); delete(s.m,b.Value.(*kv).k); s.l.Remove(b) } }
func main(){ c:=New(2); c.Put(1,1); c.Put(2,2); fmt.Println(c.Get(1)); c.Put(3,3); fmt.Println(c.Get(2)) }
