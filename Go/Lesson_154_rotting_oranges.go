//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 154 -- Rotting Oranges
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 77
// =============================================================
//
// QUESTION:
//   0 empty, 1 fresh, 2 rotten. Each minute rotten infects 4-neighbor fresh. Min minutes to rot all, or -1.
// =============================================================
package main
import "fmt"
func rot(g [][]int) int { m,n:=len(g),len(g[0]); var q [][3]int; fresh:=0; for i:=0;i<m;i++ { for j:=0;j<n;j++ { if g[i][j]==2 { q=append(q,[3]int{i,j,0}) } else if g[i][j]==1 { fresh++ } } }; t:=0; D:=[4][2]int{{-1,0},{1,0},{0,-1},{0,1}}; for len(q)>0 { p:=q[0]; q=q[1:]; t=p[2]; for _,d:=range D { ni,nj:=p[0]+d[0],p[1]+d[1]; if ni>=0 && nj>=0 && ni<m && nj<n && g[ni][nj]==1 { g[ni][nj]=2; fresh--; q=append(q,[3]int{ni,nj,p[2]+1}) } } }; if fresh>0 { return -1 }; return t }
func main(){ fmt.Println(rot([][]int{{2,1,1},{1,1,0},{0,1,1}})); fmt.Println(rot([][]int{{2,1,1},{0,1,1},{1,0,1}})) }
