//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 216 -- Partition Labels
// Category   : Greedy
// Difficulty : Medium
// Study Plan : Day 108
// =============================================================
//
// QUESTION:
//   Partition string so each char appears in at most one part. Return sizes.
// =============================================================
package main
import "fmt"
func partitionLabels(s string) []int { var last [26]int; for i:=0;i<len(s);i++ { last[s[i]-'a']=i }; r:=[]int{}; st,e:=0,0; for i:=0;i<len(s);i++ { if last[s[i]-'a']>e { e=last[s[i]-'a'] }; if i==e { r=append(r,e-st+1); st=i+1 } }; return r }
func main(){ fmt.Println(partitionLabels("ababcbacadefegdehijhklij")) }
