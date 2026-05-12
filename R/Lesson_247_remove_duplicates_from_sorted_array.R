# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 247 -- Remove Duplicates From Sorted Array
# Category   : Two Pointers
# Difficulty : Easy
# Study Plan : Day 124
# =============================================================
#
# QUESTION:
#   In-place dedupe of sorted array. Return new length.
# =============================================================
dedupe <- function(a){ length(unique(a)) }
cat(dedupe(c(1,1,2,2,3)),"\n")
