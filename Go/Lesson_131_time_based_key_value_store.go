//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 131 -- Time Based Key Value Store
// Category   : Binary Search
// Difficulty : Medium
// Study Plan : Day 66
// =============================================================
//
// QUESTION:
//   Design TimeMap: set(k,v,t) and get(k,t) returns value with greatest timestamp <= t.
// =============================================================
package main
import "fmt"
type TimeMap struct{ ts map[string][]int; vs map[string][]string }
func New() *TimeMap { return &TimeMap{map[string][]int{},map[string][]string{}} }
func (m *TimeMap) Set(k,v string,t int){ m.ts[k]=append(m.ts[k],t); m.vs[k]=append(m.vs[k],v) }
func (m *TimeMap) Get(k string,t int) string { ts,ok:=m.ts[k]; if !ok { return "" }; lo,hi,r:=0,len(ts)-1,-1; for lo<=hi { mid:=(lo+hi)/2; if ts[mid]<=t { r=mid; lo=mid+1 } else { hi=mid-1 } }; if r<0 { return "" }; return m.vs[k][r] }
func main(){ tm:=New(); tm.Set("foo","bar",1); fmt.Println(tm.Get("foo",1)); fmt.Println(tm.Get("foo",3)); tm.Set("foo","bar2",4); fmt.Println(tm.Get("foo",4)); fmt.Println(tm.Get("foo",5)) }
