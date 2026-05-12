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

var isValidSudoku = function(board){
    const seen = new Set();
    for (let i=0;i<9;i++) for (let j=0;j<9;j++){
        const v = board[i][j]; if (v===".") continue;
        const k = [`r${i}${v}`, `c${j}${v}`, `b${(i/3|0)}${(j/3|0)}${v}`];
        for (const x of k){ if (seen.has(x)) return false; seen.add(x); }
    }
    return true;
};
const b = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]];
console.log(isValidSudoku(b));
