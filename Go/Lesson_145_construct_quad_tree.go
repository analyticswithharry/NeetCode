//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 145 -- Construct Quad Tree
// Category   : Trees
// Difficulty : Medium
// Study Plan : Day 73
// =============================================================
//
// QUESTION:
//   Given an n x n grid of 0/1, build a quad tree representation. Return root.
// =============================================================
package main
import "fmt"
type QN struct{ Val,IsLeaf bool; TL,TR,BL,BR *QN }
var G [][]int
func rec(r,c,n int) *QN { same:=true; for i:=r;i<r+n;i++ { for j:=c;j<c+n;j++ { if G[i][j]!=G[r][c] { same=false } } }; if same { return &QN{G[r][c]==1,true,nil,nil,nil,nil} }; h:=n/2; return &QN{true,false,rec(r,c,h),rec(r,c+h,h),rec(r+h,c,h),rec(r+h,c+h,h)} }
func ser(n *QN) []string { if n.IsLeaf { if n.Val { return []string{"1"} }; return []string{"0"} }; r:=[]string{"#"}; r=append(r,ser(n.TL)...); r=append(r,ser(n.TR)...); r=append(r,ser(n.BL)...); r=append(r,ser(n.BR)...); return r }
func main(){ G=[][]int{{0,1},{1,0}}; fmt.Println(ser(rec(0,0,2))) }
