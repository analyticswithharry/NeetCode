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

isValidSudoku <- function(b){
    seen <- c()
    for (i in 1:9) for (j in 1:9){
        v <- b[i,j]; if (v==".") next
        keys <- c(paste0("r",i,v), paste0("c",j,v), paste0("b",(i-1)%/%3,(j-1)%/%3,v))
        if (any(keys %in% seen)) return(FALSE)
        seen <- c(seen, keys)
    }
    TRUE
}
b <- matrix(c("5","3",".",".","7",".",".",".",".",
              "6",".",".","1","9","5",".",".",".",
              ".","9","8",".",".",".",".","6",".",
              "8",".",".",".","6",".",".",".","3",
              "4",".",".","8",".","3",".",".","1",
              "7",".",".",".","2",".",".",".","6",
              ".","6",".",".",".",".","2","8",".",
              ".",".",".","4","1","9",".",".","5",
              ".",".",".",".","8",".",".","7","9"), nrow=9, byrow=TRUE)
print(isValidSudoku(b))
