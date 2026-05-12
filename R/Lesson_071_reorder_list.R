# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 071 -- Reorder List
# Category   : Linked List
# Difficulty : Medium
# Study Plan : Day 36
# =============================================================
#
# QUESTION:
#   Reorder L0 -> L1 -> ... -> Ln-1 -> Ln to L0 -> Ln -> L1 -> Ln-1 -> ...
#
#   Example: 1->2->3->4 -> 1->4->2->3
# =============================================================

reorderList <- function(a){
    n <- length(a); out <- c(); l <- 1; r <- n
    while (l <= r){ out <- c(out, a[l]); if (l != r) out <- c(out, a[r]); l <- l+1; r <- r-1 }
    out
}
print(reorderList(c(1,2,3,4)))
print(reorderList(c(1,2,3,4,5)))
