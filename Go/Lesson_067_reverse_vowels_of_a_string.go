//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 067 -- Reverse Vowels of a String
// Category   : Two Pointers
// Difficulty : Easy
// Study Plan : Day 34
// =============================================================
//
// QUESTION:
//   Reverse only the vowels of a string. Vowels: a,e,i,o,u (and uppercase).
//
//   Example: hello -> holle
// =============================================================

package main
import "fmt"
func reverseVowels(s string) string {
    v := "aeiouAEIOU"; a := []byte(s); l,r := 0,len(a)-1
    isV := func(c byte) bool { for i:=0;i<len(v);i++ { if v[i]==c { return true } }; return false }
    for l<r {
        for l<r && !isV(a[l]) { l++ }
        for l<r && !isV(a[r]) { r-- }
        a[l],a[r] = a[r],a[l]; l++; r--
    }
    return string(a)
}
func main(){ fmt.Println(reverseVowels("hello"), reverseVowels("leetcode")) }
