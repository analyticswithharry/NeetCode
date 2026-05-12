# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 075 -- Merge K Sorted Lists
# Category   : Linked List
# Difficulty : Hard
# Study Plan : Day 38
# =============================================================
#
# QUESTION:
#   Merge k sorted linked lists into one sorted list.
#
#   Example: [[1,4,5],[1,3,4],[2,6]] -> 1->1->2->3->4->4->5->6
# =============================================================

mergeKLists <- function(lists) sort(unlist(lists))
print(mergeKLists(list(c(1,4,5), c(1,3,4), c(2,6))))
