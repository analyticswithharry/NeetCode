# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 230 -- Integer Break
# Category   : 1-D Dynamic Programming
# Difficulty : Medium
# Study Plan : Day 115
# =============================================================
#
# QUESTION:
#   Break n into >=2 positive ints; maximize product.
# =============================================================
integerBreak <- function(n){ dp<-rep(0,n+1); dp[2]<-1; for(i in 2:n) for(j in 1:(i-1)) dp[i+1]<-max(dp[i+1], j*max(i-j,dp[i-j+1])); dp[n+1] }
cat(integerBreak(10),"\n")
