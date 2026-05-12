# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 062 -- Valid Sudoku
# Category   : Arrays and Hashing
# Difficulty : Medium
# Study Plan : Day 31
# =============================================================
#
# QUESTION:
#   Determine if a 9x9 Sudoku board is valid (no duplicates in any row, column, or 3x3 box). Empty cells are '.'.
# =============================================================

class Solution:
    def isValidSudoku(self, board):
        seen = set()
        for i in range(9):
            for j in range(9):
                v = board[i][j]
                if v == ".": continue
                items = [(v,"r",i),(v,"c",j),(v,"b",i//3,j//3)]
                for it in items:
                    if it in seen: return False
                    seen.add(it)
        return True

if __name__ == "__main__":
    b = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]
    print(Solution().isValidSudoku(b))
