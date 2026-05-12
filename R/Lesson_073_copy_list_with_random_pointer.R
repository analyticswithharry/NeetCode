# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 073 -- Copy List With Random Pointer
# Category   : Linked List
# Difficulty : Medium
# Study Plan : Day 37
# =============================================================
#
# QUESTION:
#   Deep copy a linked list where each node has next and a random pointer that may point to any node or null.
# =============================================================

# Emulate with a data.frame: val, next_idx, random_idx
copyRandomList <- function(df){
    df2 <- df  # already a value copy in R
    df2
}
df <- data.frame(val=c(1,2), next_idx=c(2,NA), random_idx=c(2,2))
print(copyRandomList(df))
