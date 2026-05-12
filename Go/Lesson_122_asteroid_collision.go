//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 122 -- Asteroid Collision
// Category   : Stack
// Difficulty : Medium
// Study Plan : Day 61
// =============================================================
//
// QUESTION:
//   Given an array of asteroids (positive=right, negative=left), return state after all collisions.
// =============================================================
package main
import "fmt"
func collide(a []int) []int { var st []int; outer: for _,x:=range a { for len(st)>0 && x<0 && st[len(st)-1]>0 { if st[len(st)-1]<-x { st=st[:len(st)-1]; continue }; if st[len(st)-1]==-x { st=st[:len(st)-1] }; continue outer }; st=append(st,x) }; return st }
func main(){ fmt.Println(collide([]int{5,10,-5})); fmt.Println(collide([]int{8,-8})); fmt.Println(collide([]int{10,2,-5})) }
