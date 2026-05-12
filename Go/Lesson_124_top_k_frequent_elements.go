//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 124 -- Top K Frequent Elements
// Category   : Arrays and Hashing
// Difficulty : Medium
// Study Plan : Day 62
// =============================================================
//
// QUESTION:
//   Given an integer array nums and integer k, return the k most frequent elements.
// =============================================================
package main
import ("fmt";"sort")
func topK(a []int,k int) []int { m:=map[int]int{}; for _,x:=range a { m[x]++ }; type P struct{V,C int}; var v []P; for kk,c:=range m { v=append(v,P{kk,c}) }; sort.Slice(v,func(i,j int) bool{return v[i].C>v[j].C}); r:=make([]int,k); for i:=0;i<k;i++ { r[i]=v[i].V }; return r }
func main(){ fmt.Println(topK([]int{1,1,1,2,2,3},2)) }
