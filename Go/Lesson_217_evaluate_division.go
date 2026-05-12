//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 217 -- Evaluate Division
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 109
// =============================================================
//
// QUESTION:
//   Given equations a/b=value, answer queries x/y. Build weighted graph and DFS.
// =============================================================
package main
import "fmt"
var g=map[string]map[string]float64{}
func dfs(s,t string, seen map[string]bool) float64 { if _,ok:=g[s];!ok { return -1 }; if _,ok:=g[t];!ok { return -1 }; if s==t { return 1 }; seen[s]=true; for n,w:=range g[s] { if seen[n] { continue }; r:=dfs(n,t,seen); if r!=-1 { return w*r } }; return -1 }
func main(){ eq:=[][2]string{{"a","b"},{"b","c"}}; v:=[]float64{2,3}; for i:=range eq { if g[eq[i][0]]==nil{g[eq[i][0]]=map[string]float64{}}; if g[eq[i][1]]==nil{g[eq[i][1]]=map[string]float64{}}; g[eq[i][0]][eq[i][1]]=v[i]; g[eq[i][1]][eq[i][0]]=1/v[i] }; fmt.Println(dfs("a","c",map[string]bool{})) }
