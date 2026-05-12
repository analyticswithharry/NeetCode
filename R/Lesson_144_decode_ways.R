# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 144 -- Decode Ways
# Category   : 1-D Dynamic Programming
# Difficulty : Medium
# Study Plan : Day 72
# =============================================================
#
# QUESTION:
#   Number of ways to decode digit string s where '1'->A, ..., '26'->Z.
# =============================================================
ways <- function(s){ if(nchar(s)==0 || substr(s,1,1)=="0") return(0); n<-nchar(s); dp<-rep(0,n+1); dp[1]<-1; dp[2]<-1; if(n>=2) for(i in 2:n){ if(substr(s,i,i)!="0") dp[i+1]<-dp[i+1]+dp[i]; x<-as.integer(substr(s,i-1,i)); if(x>=10 && x<=26) dp[i+1]<-dp[i+1]+dp[i-1] }; dp[n+1] }
cat(ways("12"),"\n"); cat(ways("226"),"\n"); cat(ways("06"),"\n")
