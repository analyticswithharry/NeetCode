# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 069 -- Add Two Numbers
# Category   : Linked List
# Difficulty : Medium
# Study Plan : Day 35
# =============================================================
#
# QUESTION:
#   Two non-empty linked lists representing non-negative integers in reverse order. Return sum as linked list.
#
#   Example: 2->4->3 + 5->6->4 = 7->0->8 (i.e., 342 + 465 = 807)
# =============================================================

addTwoNumbers <- function(a, b){
    n <- max(length(a), length(b)); a <- c(a, rep(0, n-length(a))); b <- c(b, rep(0, n-length(b)))
    out <- c(); carry <- 0
    for (i in 1:n){ s <- a[i]+b[i]+carry; carry <- s %/% 10; out <- c(out, s %% 10) }
    if (carry > 0) out <- c(out, carry)
    out
}
print(addTwoNumbers(c(2,4,3), c(5,6,4)))
