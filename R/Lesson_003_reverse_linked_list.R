# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 003 -- Reverse Linked List
# Category   : Linked List
# Difficulty : Easy
# Study Plan : Day 2
# =============================================================
#
# QUESTION:
#   Given the head of a singly linked list, reverse the list and return
#   the new head.
#
#   Example:
#     Input : 1 -> 2 -> 3 -> 4 -> 5
#     Output: 5 -> 4 -> 3 -> 2 -> 1
# =============================================================

# R lacks built-in linked list; represent as a vector and reverse.
reverseList <- function(v) rev(v)
print(reverseList(c(1,2,3,4,5)))  # 5 4 3 2 1
