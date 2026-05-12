//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 231 -- Encode and Decode Strings
// Category   : Arrays and Hashing
// Difficulty : Medium
// Study Plan : Day 116
// =============================================================
//
// QUESTION:
//   Length-prefix encoding for arbitrary strings.
// =============================================================
package main
import ("fmt";"strconv";"strings")
func encode(a []string) string { var b strings.Builder; for _,s:=range a { fmt.Fprintf(&b,"%d#%s",len(s),s) }; return b.String() }
func decode(s string) []string { r:=[]string{}; i:=0; for i<len(s) { j:=strings.Index(s[i:],"#")+i; n,_:=strconv.Atoi(s[i:j]); r=append(r,s[j+1:j+1+n]); i=j+1+n }; return r }
func main(){ e:=encode([]string{"hello","world","#42"}); fmt.Println(e); fmt.Println(decode(e)) }
