# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 133 -- Counting Bits
# Category   : Bit Manipulation
# Difficulty : Easy
# Study Plan : Day 67
# =============================================================
#
# QUESTION:
#   For 0..n return array where ans[i] = number of 1-bits in i.
# =============================================================
cb <- function(n){ a<-rep(0,n+1); for(i in 1:n) a[i+1]<-a[(i %/% 2)+1] + (i %% 2); a }
print(cb(5))
