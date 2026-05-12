# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 236 -- Valid Sudoku
# Category   : Arrays and Hashing
# Difficulty : Medium
# Study Plan : Day 118
# =============================================================
#
# QUESTION:
#   Validate 9x9 board: rows, cols, 3x3 boxes have unique 1-9 (ignore '.').
# =============================================================
def isValid(b):
    rows=[set() for _ in range(9)]; cols=[set() for _ in range(9)]; box=[set() for _ in range(9)]
    for i in range(9):
        for j in range(9):
            c=b[i][j]
            if c=='.': continue
            k=(i//3)*3+j//3
            if c in rows[i] or c in cols[j] or c in box[k]: return False
            rows[i].add(c); cols[j].add(c); box[k].add(c)
    return True
if __name__=="__main__":
    bd=[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    print(isValid(bd))
