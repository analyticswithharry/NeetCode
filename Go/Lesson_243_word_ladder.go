//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 243 -- Word Ladder
// Category   : Graphs
// Difficulty : Hard
// Study Plan : Day 122
// =============================================================
//
// QUESTION:
//   Shortest transformation sequence length from begin to end. BFS with wildcard buckets.
// =============================================================
package main
import "fmt"
func ladderLength(b,e string, wl []string) int { ws:=map[string]bool{}; for _,w:=range wl{ws[w]=true}; if !ws[e]{return 0}; L:=len(b); buc:=map[string][]string{}; for w:=range ws { for i:=0;i<L;i++ { k:=w[:i]+"*"+w[i+1:]; buc[k]=append(buc[k],w) } }; type S struct{w string; d int}; q:=[]S{{b,1}}; seen:=map[string]bool{b:true}; for len(q)>0 { x:=q[0]; q=q[1:]; if x.w==e {return x.d}; for i:=0;i<L;i++ { k:=x.w[:i]+"*"+x.w[i+1:]; for _,n:=range buc[k] { if !seen[n] { seen[n]=true; q=append(q,S{n,x.d+1}) } } } }; return 0 }
func main(){ fmt.Println(ladderLength("hit","cog",[]string{"hot","dot","dog","lot","log","cog"})) }
