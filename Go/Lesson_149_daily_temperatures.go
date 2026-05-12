//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 149 -- Daily Temperatures
// Category   : Stack
// Difficulty : Medium
// Study Plan : Day 75
// =============================================================
//
// QUESTION:
//   For each day, return number of days until a warmer temperature, or 0.
// =============================================================
package main
import "fmt"
func dailyT(t []int) []int { r:=make([]int,len(t)); var st []int; for i,x:=range t { for len(st)>0 && t[st[len(st)-1]]<x { j:=st[len(st)-1]; st=st[:len(st)-1]; r[j]=i-j }; st=append(st,i) }; return r }
func main(){ fmt.Println(dailyT([]int{73,74,75,71,69,72,76,73})) }
