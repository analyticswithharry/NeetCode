# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 004 -- Merge Two Sorted Lists
# Category   : Linked List
# Difficulty : Easy
# Study Plan : Day 2
# =============================================================
#
# QUESTION:
#   You are given the heads of two sorted linked lists list1 and list2.
#   Merge them into one sorted list and return its head.
#
#   Example:
#     Input : 1->2->4, 1->3->4
#     Output: 1->1->2->3->4->4
# =============================================================

# Merge two already-sorted vectors to mimic merging two sorted lists.
mergeTwoLists <- function(a, b) {
    out <- integer(length(a) + length(b)); i <- 1; j <- 1; k <- 1
    while (i <= length(a) && j <= length(b)) {
        if (a[i] <= b[j]) { out[k] <- a[i]; i <- i + 1 } else { out[k] <- b[j]; j <- j + 1 }
        k <- k + 1
    }
    while (i <= length(a)) { out[k] <- a[i]; i <- i + 1; k <- k + 1 }
    while (j <= length(b)) { out[k] <- b[j]; j <- j + 1; k <- k + 1 }
    out
}

print(mergeTwoLists(c(1,2,4), c(1,3,4)))  # 1 1 2 3 4 4
