# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 070 -- Remove Nth Node From End of List
# Category   : Linked List
# Difficulty : Medium
# Study Plan : Day 35
# =============================================================
#
# QUESTION:
#   Remove the nth node from the end of a linked list and return its head.
#
#   Example: head = 1->2->3->4->5, n = 2 -> 1->2->3->5
# =============================================================

removeNthFromEnd <- function(a, n){ a[-(length(a)-n+1)] }
print(removeNthFromEnd(c(1,2,3,4,5), 2))
