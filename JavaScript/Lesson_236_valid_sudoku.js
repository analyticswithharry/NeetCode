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
function isValid(b){const r=Array.from({length:9},()=>new Set()),c=Array.from({length:9},()=>new Set()),x=Array.from({length:9},()=>new Set());for(let i=0;i<9;i++)for(let j=0;j<9;j++){const v=b[i][j];if(v===".")continue;const k=Math.floor(i/3)*3+Math.floor(j/3);if(r[i].has(v)||c[j].has(v)||x[k].has(v))return false;r[i].add(v);c[j].add(v);x[k].add(v);}return true;}
console.log(isValid([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]));
