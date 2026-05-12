//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 156 -- Greatest Common Divisor Traversal
// Category   : Advanced Graphs
// Difficulty : Hard
// Study Plan : Day 78
// =============================================================
//
// QUESTION:
//   You can move between indices i,j if gcd(nums[i],nums[j])>1. Return true iff every pair is connected.
// =============================================================
package main
import "fmt"
var par []int
func f(x int) int { for par[x]!=x { par[x]=par[par[x]]; x=par[x] }; return x }
func u(x,y int){ x=f(x); y=f(y); if x!=y { par[x]=y } }
func primes(x int) []int { var r []int; for d:=2;d*d<=x;d++ { if x%d==0 { r=append(r,d); for x%d==0 { x/=d } } }; if x>1 { r=append(r,x) }; return r }
func can(a []int) bool { n:=len(a); par=make([]int,n); for i:=range par { par[i]=i }; pm:=map[int]int{}; for i:=0;i<n;i++ { for _,p:=range primes(a[i]) { if v,ok:=pm[p]; ok { u(i,v) } else { pm[p]=i } } }; r:=f(0); for i:=0;i<n;i++ { if f(i)!=r { return false } }; return true }
func main(){ fmt.Println(can([]int{2,3,6})); fmt.Println(can([]int{3,9,5})); fmt.Println(can([]int{4,3,12,8})) }
