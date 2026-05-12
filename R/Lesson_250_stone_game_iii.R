# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 250 -- Stone Game III
# Category   : 1-D Dynamic Programming
# Difficulty : Hard
# Study Plan : Day 125
# =============================================================
#
# QUESTION:
#   Players take 1-3 stones from front; maximize own score. Return Alice/Bob/Tie.
# =============================================================
stoneGameIII <- function(s){ n<-length(s); dp<-rep(0,n+1); for(i in n:1){ best<--Inf; take<-0; for(k in 0:2){ if(i+k>n) break; take<-take+s[i+k]; best<-max(best,take-dp[i+k+1]) }; dp[i]<-best }; if(dp[1]>0) "Alice" else if(dp[1]<0) "Bob" else "Tie" }
cat(stoneGameIII(c(1,2,3,7)),"\n")
