# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 225 -- Partition Equal Subset Sum
# Category   : 1-D Dynamic Programming
# Difficulty : Medium
# Study Plan : Day 113
# =============================================================
#
# QUESTION:
#   Can the array be split into two equal-sum subsets? Subset-sum DP.
# =============================================================
canPartition <- function(nums){ s<-sum(nums); if(s%%2==1) return(FALSE); t<-s/2; dp<-c(TRUE,rep(FALSE,t)); for(x in nums) for(v in seq(t,x,-1)) dp[v+1]<-dp[v+1]||dp[v-x+1]; dp[t+1] }
cat(canPartition(c(1,5,11,5)),"\n")
