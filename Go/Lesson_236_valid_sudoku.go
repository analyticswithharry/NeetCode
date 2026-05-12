//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 236 -- Valid Sudoku
// Category   : Arrays and Hashing
// Difficulty : Medium
// Study Plan : Day 118
// =============================================================
//
// QUESTION:
//   Validate 9x9 board: rows, cols, 3x3 boxes have unique 1-9 (ignore '.').
// =============================================================
package main
import "fmt"
func isValid(b [][]byte) bool { var r,c,x [9][10]bool; for i:=0;i<9;i++ { for j:=0;j<9;j++ { v:=b[i][j]; if v=='.'{continue}; n:=int(v-'0'); k:=(i/3)*3+j/3; if r[i][n]||c[j][n]||x[k][n]{return false}; r[i][n]=true; c[j][n]=true; x[k][n]=true } }; return true }
func main(){ bd:=[][]byte{{'5','3','.','.','7','.','.','.','.'},{'6','.','.','1','9','5','.','.','.'},{'.','9','8','.','.','.','.','6','.'},{'8','.','.','.','6','.','.','.','3'},{'4','.','.','8','.','3','.','.','1'},{'7','.','.','.','2','.','.','.','6'},{'.','6','.','.','.','.','2','8','.'},{'.','.','.','4','1','9','.','.','5'},{'.','.','.','.','8','.','.','7','9'}}; fmt.Println(isValid(bd)) }
