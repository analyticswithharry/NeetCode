//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 249 -- Serialize And Deserialize Binary Tree
// Category   : Trees
// Difficulty : Hard
// Study Plan : Day 125
// =============================================================
//
// QUESTION:
//   Pre-order serialize with null markers; queue-based deserialize.
// =============================================================
package main
import ("fmt";"strconv";"strings")
type T struct{v int; l,r *T}
func dfs(n *T, sb *strings.Builder){ if n==nil { sb.WriteString("#,"); return }; sb.WriteString(strconv.Itoa(n.v)); sb.WriteString(","); dfs(n.l,sb); dfs(n.r,sb) }
func ser(r *T) string { var sb strings.Builder; dfs(r,&sb); return sb.String() }
var idx int; var arr []string
func dfs2() *T { x:=arr[idx]; idx++; if x=="#" { return nil }; v,_:=strconv.Atoi(x); n:=&T{v:v}; n.l=dfs2(); n.r=dfs2(); return n }
func des(s string) *T { arr=strings.Split(s,","); idx=0; return dfs2() }
func main(){ r:=&T{v:1,l:&T{v:2},r:&T{v:3,l:&T{v:4},r:&T{v:5}}}; s:=ser(r); fmt.Println(s); fmt.Println(ser(des(s))) }
