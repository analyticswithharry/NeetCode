//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 232 -- Range Sum Query 2D Immutable
// Category   : Arrays and Hashing
// Difficulty : Medium
// Study Plan : Day 116
// =============================================================
//
// QUESTION:
//   Build prefix sum 2D for O(1) region queries.
// =============================================================
package main
import "fmt"
type NM struct{p [][]int}
func New(m [][]int) *NM { R,C:=len(m),len(m[0]); p:=make([][]int,R+1); for i:=range p{p[i]=make([]int,C+1)}; for i:=0;i<R;i++ { for j:=0;j<C;j++ { p[i+1][j+1]=m[i][j]+p[i][j+1]+p[i+1][j]-p[i][j] } }; return &NM{p} }
func (n *NM) SumRegion(r1,c1,r2,c2 int) int { return n.p[r2+1][c2+1]-n.p[r1][c2+1]-n.p[r2+1][c1]+n.p[r1][c1] }
func main(){ n:=New([][]int{{3,0,1},{5,6,3},{1,2,0}}); fmt.Println(n.SumRegion(0,0,2,2)); fmt.Println(n.SumRegion(1,1,2,2)) }
