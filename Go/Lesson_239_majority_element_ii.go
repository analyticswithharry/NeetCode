//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 239 -- Majority Element II
// Category   : Arrays and Hashing
// Difficulty : Medium
// Study Plan : Day 120
// =============================================================
//
// QUESTION:
//   All elements appearing more than n/3 times. Boyer-Moore variant.
// =============================================================
package main
import "fmt"
func majorityIII(nums []int) []int { c1,c2,n1,n2:=0,0,0,1; for _,x:=range nums { if x==n1{c1++}else if x==n2{c2++}else if c1==0{n1=x;c1=1}else if c2==0{n2=x;c2=1}else{c1--;c2--} }; r:=[]int{}; for _,n:=range []int{n1,n2}{ cnt:=0; for _,x:=range nums{ if x==n{cnt++} }; if cnt>len(nums)/3 { dup:=false; for _,y:=range r{if y==n{dup=true}}; if !dup { r=append(r,n) } } }; return r }
func main(){ fmt.Println(majorityIII([]int{1,1,1,3,3,2,2,2})) }
