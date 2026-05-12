//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 116 -- Spiral Matrix
// Category   : Math and Geometry
// Difficulty : Medium
// Study Plan : Day 58
// =============================================================
//
// QUESTION:
//   Given m x n matrix, return all elements in spiral order.
// =============================================================
package main
import "fmt"
func spiral(m [][]int) []int { var r []int; if len(m)==0 { return r }; t,b,l,rg:=0,len(m)-1,0,len(m[0])-1; for t<=b && l<=rg { for j:=l;j<=rg;j++ { r=append(r,m[t][j]) }; t++; for i:=t;i<=b;i++ { r=append(r,m[i][rg]) }; rg--; if t<=b { for j:=rg;j>=l;j-- { r=append(r,m[b][j]) }; b-- }; if l<=rg { for i:=b;i>=t;i-- { r=append(r,m[i][l]) }; l++ } }; return r }
func main(){ fmt.Println(spiral([][]int{{1,2,3},{4,5,6},{7,8,9}})) }
