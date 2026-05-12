# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 147 -- Last Stone Weight II
# Category   : 2-D Dynamic Programming
# Difficulty : Medium
# Study Plan : Day 74
# =============================================================
#
# QUESTION:
#   Given stones, smash to minimize remaining weight (subset partition).
# =============================================================
lsw2 <- function(s){ t<-sum(s); cap<-t %/% 2; dp<-rep(FALSE,cap+1); dp[1]<-TRUE; for(x in s) for(j in (cap+1):(x+1)) if(j-x>=1 && dp[j-x]) dp[j]<-TRUE; for(j in (cap+1):1) if(dp[j]) return(t-2*(j-1)); 0 }
cat(lsw2(c(2,7,4,1,8,1)),"\n"); cat(lsw2(c(31,26,33,21,40)),"\n")
