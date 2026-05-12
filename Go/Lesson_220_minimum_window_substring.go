//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 220 -- Minimum Window Substring
// Category   : Sliding Window
// Difficulty : Hard
// Study Plan : Day 110
// =============================================================
//
// QUESTION:
//   Smallest substring of s containing all chars of t.
// =============================================================
package main
import "fmt"
func minWindow(s,t string) string { if t==""{return""}; need:=map[byte]int{}; have:=map[byte]int{}; for i:=0;i<len(t);i++{need[t[i]]++}; nn:=len(need); hn:=0; l:=0; rl:=1<<30; rs:=0; for r:=0;r<len(s);r++ { have[s[r]]++; if need[s[r]]>0 && have[s[r]]==need[s[r]]{ hn++ }; for hn==nn { if r-l+1<rl { rl=r-l+1; rs=l }; have[s[l]]--; if need[s[l]]>0 && have[s[l]]<need[s[l]]{ hn-- }; l++ } }; if rl==1<<30 { return "" }; return s[rs:rs+rl] }
func main(){ fmt.Println(minWindow("ADOBECODEBANC","ABC")) }
