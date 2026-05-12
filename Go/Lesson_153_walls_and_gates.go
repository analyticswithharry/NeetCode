//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 153 -- Walls And Gates
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 77
// =============================================================
//
// QUESTION:
//   Grid: -1 wall, 0 gate, INF empty. Fill each empty with distance to nearest gate.
// =============================================================
package main
import "fmt"
const INF = 2147483647
func walls(g [][]int) [][]int { if len(g)==0 { return g }; m,n:=len(g),len(g[0]); var q [][2]int; for i:=0;i<m;i++ { for j:=0;j<n;j++ { if g[i][j]==0 { q=append(q,[2]int{i,j}) } } }; D:=[4][2]int{{-1,0},{1,0},{0,-1},{0,1}}; for len(q)>0 { p:=q[0]; q=q[1:]; for _,d:=range D { ni,nj:=p[0]+d[0],p[1]+d[1]; if ni>=0 && nj>=0 && ni<m && nj<n && g[ni][nj]==INF { g[ni][nj]=g[p[0]][p[1]]+1; q=append(q,[2]int{ni,nj}) } } }; return g }
func main(){ g:=[][]int{{INF,-1,0,INF},{INF,INF,INF,-1},{INF,-1,INF,-1},{0,-1,INF,INF}}; fmt.Println(walls(g)) }
