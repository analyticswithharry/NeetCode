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

import java.util.*;
public class Lesson062_ValidSudoku {
    public boolean isValidSudoku(char[][] b){
        Set<String> s = new HashSet<>();
        for (int i=0;i<9;i++) for (int j=0;j<9;j++){
            char v = b[i][j]; if (v=='.') continue;
            if (!s.add("r"+i+v) || !s.add("c"+j+v) || !s.add("b"+(i/3)+(j/3)+v)) return false;
        }
        return true;
    }
    public static void main(String[] a){
        char[][] b = {
            {'5','3','.','.','7','.','.','.','.'},{'6','.','.','1','9','5','.','.','.'},
            {'.','9','8','.','.','.','.','6','.'},{'8','.','.','.','6','.','.','.','3'},
            {'4','.','.','8','.','3','.','.','1'},{'7','.','.','.','2','.','.','.','6'},
            {'.','6','.','.','.','.','2','8','.'},{'.','.','.','4','1','9','.','.','5'},
            {'.','.','.','.','8','.','.','7','9'}};
        System.out.println(new Lesson062_ValidSudoku().isValidSudoku(b));
    }
}
