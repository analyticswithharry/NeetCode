# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 223 -- Burst Balloons
# Category   : 2-D Dynamic Programming
# Difficulty : Hard
# Study Plan : Day 112
# =============================================================
#
# QUESTION:
#   Burst balloons; coins = nums[l]*nums[i]*nums[r]. Maximize total.
# =============================================================
maxCoins <- function(nums){ a<-c(1,nums,1); n<-length(a); dp<-matrix(0,n,n); for(L in 2:(n-1)) for(l in 1:(n-L)){ r<-l+L; for(i in (l+1):(r-1)) dp[l,r]<-max(dp[l,r],dp[l,i]+dp[i,r]+a[l]*a[i]*a[r]) }; dp[1,n] }
cat(maxCoins(c(3,1,5,8)),"\n")
