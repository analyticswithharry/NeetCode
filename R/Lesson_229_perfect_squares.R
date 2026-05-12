# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 229 -- Perfect Squares
# Category   : 1-D Dynamic Programming
# Difficulty : Medium
# Study Plan : Day 115
# =============================================================
#
# QUESTION:
#   Min number of perfect-square numbers summing to n.
# =============================================================
numSquares <- function(n){ dp<-c(0,rep(Inf,n)); for(i in 1:n){ j<-1; while(j*j<=i){ dp[i+1]<-min(dp[i+1],dp[i-j*j+1]+1); j<-j+1 } }; dp[n+1] }
cat(numSquares(12),"\n")
