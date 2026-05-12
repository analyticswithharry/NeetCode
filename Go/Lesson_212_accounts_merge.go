//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 212 -- Accounts Merge
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 106
// =============================================================
//
// QUESTION:
//   Merge accounts that share any common email. Return merged accounts with name + sorted unique emails.
// =============================================================
package main
import ("fmt";"sort")
var p,own=map[string]string{},map[string]string{}
func f(x string) string { for p[x]!=x { p[x]=p[p[x]]; x=p[x] }; return x }
func main(){ acc:=[][]string{{"A","a@x","b@x"},{"A","b@x","c@x"},{"B","d@x"}}; for _,a:=range acc { for i:=1;i<len(a);i++ { if _,ok:=p[a[i]];!ok { p[a[i]]=a[i] }; own[a[i]]=a[0]; p[f(a[i])]=f(a[1]) } }; g:=map[string][]string{}; for k:=range p { r:=f(k); g[r]=append(g[r],k) }; for _,v:=range g { sort.Strings(v); fmt.Println(append([]string{own[v[0]]},v...)) } }
