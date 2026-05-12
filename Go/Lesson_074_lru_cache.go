//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 074 -- LRU Cache
// Category   : Linked List
// Difficulty : Medium
// Study Plan : Day 37
// =============================================================
//
// QUESTION:
//   Design an LRU cache with O(1) get and put.
// =============================================================

package main
import ("container/list"; "fmt")
type LRUCache struct { cap int; l *list.List; m map[int]*list.Element }
type entry struct { k, v int }
func Constructor(cap int) LRUCache { return LRUCache{cap: cap, l: list.New(), m: map[int]*list.Element{}} }
func (c *LRUCache) Get(k int) int {
    if e, ok := c.m[k]; ok { c.l.MoveToFront(e); return e.Value.(*entry).v }
    return -1
}
func (c *LRUCache) Put(k, v int) {
    if e, ok := c.m[k]; ok { e.Value.(*entry).v = v; c.l.MoveToFront(e); return }
    e := c.l.PushFront(&entry{k,v}); c.m[k] = e
    if c.l.Len() > c.cap { b := c.l.Back(); delete(c.m, b.Value.(*entry).k); c.l.Remove(b) }
}
func main(){ c := Constructor(2); c.Put(1,1); c.Put(2,2); fmt.Println(c.Get(1))
    c.Put(3,3); fmt.Println(c.Get(2)); c.Put(4,4); fmt.Println(c.Get(1), c.Get(3), c.Get(4)) }
