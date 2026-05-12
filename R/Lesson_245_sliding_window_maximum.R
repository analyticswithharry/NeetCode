# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 245 -- Sliding Window Maximum
# Category   : Sliding Window
# Difficulty : Hard
# Study Plan : Day 123
# =============================================================
#
# QUESTION:
#   Max in each window of size k. Monotonic deque.
# =============================================================
maxSliding <- function(n,k){ sapply(1:(length(n)-k+1), function(i) max(n[i:(i+k-1)])) }
cat(maxSliding(c(1,3,-1,-3,5,3,6,7),3),"\n")
