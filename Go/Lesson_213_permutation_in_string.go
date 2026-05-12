//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 213 -- Permutation in String
// Category   : Sliding Window
// Difficulty : Medium
// Study Plan : Day 107
// =============================================================
//
// QUESTION:
//   Return true if s2 contains a permutation of s1.
// =============================================================
package main
import "fmt"
func checkInclusion(s1,s2 string) bool { if len(s1)>len(s2){return false}; var a,b [26]int; for _,c:=range s1 { a[c-'a']++ }; for i:=0;i<len(s2);i++ { b[s2[i]-'a']++; if i>=len(s1) { b[s2[i-len(s1)]-'a']-- }; if a==b { return true } }; return false }
func main(){ fmt.Println(checkInclusion("ab","eidbaooo")); fmt.Println(checkInclusion("ab","eidboaoo")) }
