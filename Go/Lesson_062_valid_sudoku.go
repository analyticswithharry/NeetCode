//go:build ignore

// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 062 -- Valid Sudoku
// Category   : Arrays and Hashing
// Difficulty : Medium
// Study Plan : Day 31
// =============================================================
//
// QUESTION:
//   Determine if a 9x9 Sudoku board is valid (no duplicates in any row, column, or 3x3 box). Empty cells are '.'.
// =============================================================

package main
import "fmt"
func isValidSudoku(b [][]byte) bool {
    s := map[string]bool{}
    for i:=0;i<9;i++ { for j:=0;j<9;j++ {
        v := b[i][j]; if v=='.' { continue }
        keys := []string{ fmt.Sprintf("r%d%c",i,v), fmt.Sprintf("c%d%c",j,v), fmt.Sprintf("b%d%d%c",i/3,j/3,v) }
        for _,k := range keys { if s[k] { return false }; s[k]=true }
    }}
    return true
}
func main(){
    b := [][]byte{
        {'5','3','.','.','7','.','.','.','.'},{'6','.','.','1','9','5','.','.','.'},
        {'.','9','8','.','.','.','.','6','.'},{'8','.','.','.','6','.','.','.','3'},
        {'4','.','.','8','.','3','.','.','1'},{'7','.','.','.','2','.','.','.','6'},
        {'.','6','.','.','.','.','2','8','.'},{'.','.','.','4','1','9','.','.','5'},
        {'.','.','.','.','8','.','.','7','9'}}
    fmt.Println(isValidSudoku(b))
}
