# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 226 -- Combination Sum IV
# Category   : 1-D Dynamic Programming
# Difficulty : Medium
# Study Plan : Day 113
# =============================================================
#
# QUESTION:
#   Count ordered combinations of nums summing to target.
# =============================================================
combSum4 <- function(nums,t){ dp<-c(1,rep(0,t)); for(v in 1:t) for(x in nums) if(v>=x) dp[v+1]<-dp[v+1]+dp[v-x+1]; dp[t+1] }
cat(combSum4(c(1,2,3),4),"\n")
