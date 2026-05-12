//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 144 -- Decode Ways
// Category   : 1-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 72
// =============================================================
//
// QUESTION:
//   Number of ways to decode digit string s where '1'->A, ..., '26'->Z.
// =============================================================
package main
import ("fmt";"strconv")
func ways(s string) int { if s=="" || s[0]=='0' { return 0 }; n:=len(s); dp:=make([]int,n+1); dp[0]=1; dp[1]=1; for i:=2;i<=n;i++ { if s[i-1]!='0' { dp[i]+=dp[i-1] }; x,_:=strconv.Atoi(s[i-2:i]); if x>=10 && x<=26 { dp[i]+=dp[i-2] } }; return dp[n] }
func main(){ fmt.Println(ways("12")); fmt.Println(ways("226")); fmt.Println(ways("06")) }
