# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 076 -- Reverse Nodes in k-Group
# Category   : Linked List
# Difficulty : Hard
# Study Plan : Day 38
# =============================================================
#
# QUESTION:
#   Reverse the nodes of a linked list k at a time. If fewer than k nodes remain, leave them as-is.
#
#   Example: 1->2->3->4->5, k=2 -> 2->1->4->3->5
# =============================================================

reverseKGroup <- function(a, k){
    n <- length(a); out <- a; i <- 1
    while (i + k - 1 <= n){ out[i:(i+k-1)] <- rev(out[i:(i+k-1)]); i <- i + k }
    out
}
print(reverseKGroup(c(1,2,3,4,5), 2))
print(reverseKGroup(c(1,2,3,4,5), 3))
