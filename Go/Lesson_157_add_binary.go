//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 157 -- Add Binary
// Category   : Bit Manipulation
// Difficulty : Easy
// Study Plan : Day 79
// =============================================================
//
// QUESTION:
//   Given two binary strings, return their sum as a binary string.
// =============================================================
package main
import "fmt"
func addBin(a,b string) string { i,j,c:=len(a)-1,len(b)-1,0; var r []byte; for i>=0 || j>=0 || c>0 { s:=c; if i>=0 { s+=int(a[i]-'0'); i-- }; if j>=0 { s+=int(b[j]-'0'); j-- }; r=append(r,byte('0'+s%2)); c=s/2 }; for x,y:=0,len(r)-1; x<y; x,y=x+1,y-1 { r[x],r[y]=r[y],r[x] }; return string(r) }
func main(){ fmt.Println(addBin("11","1")); fmt.Println(addBin("1010","1011")) }
