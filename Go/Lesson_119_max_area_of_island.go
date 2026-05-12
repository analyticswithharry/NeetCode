//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 119 -- Max Area of Island
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 60
// =============================================================
//
// QUESTION:
//   Given m x n binary grid, return max area of an island (4-directionally connected 1s).
// =============================================================
package main
import "fmt"
func maxArea(g [][]int) int { m,n:=len(g),len(g[0]); var dfs func(i,j int) int; dfs=func(i,j int) int { if i<0||j<0||i>=m||j>=n||g[i][j]!=1 { return 0 }; g[i][j]=0; return 1+dfs(i+1,j)+dfs(i-1,j)+dfs(i,j+1)+dfs(i,j-1) }; b:=0; for i:=0;i<m;i++ { for j:=0;j<n;j++ { if g[i][j]==1 { v:=dfs(i,j); if v>b { b=v } } } }; return b }
func main(){ fmt.Println(maxArea([][]int{{1,1,0},{1,0,0},{0,0,1}})) }
