//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 063 -- Encode and Decode Strings
// Category   : Arrays and Hashing
// Difficulty : Medium
// Study Plan : Day 32
// =============================================================
//
// QUESTION:
//   Design encode/decode of a list of strings into one string and back.
//
//   Strategy: prefix each string with its length and a delimiter (e.g., 5#hello).
// =============================================================

package main
import ("fmt"; "strconv"; "strings")
func encode(strs []string) string {
    var b strings.Builder
    for _,s := range strs { b.WriteString(strconv.Itoa(len(s))); b.WriteByte('#'); b.WriteString(s) }
    return b.String()
}
func decode(s string) []string {
    out := []string{}; i := 0
    for i < len(s) {
        j := strings.IndexByte(s[i:], '#') + i
        n,_ := strconv.Atoi(s[i:j])
        out = append(out, s[j+1:j+1+n]); i = j+1+n
    }
    return out
}
func main(){ e := encode([]string{"lint","code","love","you"}); fmt.Println(e); fmt.Println(decode(e)) }
