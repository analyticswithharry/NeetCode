# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 240 -- Subarray Sum Equals K
# Category   : Arrays and Hashing
# Difficulty : Medium
# Study Plan : Day 120
# =============================================================
#
# QUESTION:
#   Count subarrays with sum k using prefix-sum frequency map.
# =============================================================
subarraySum <- function(n,k){ m<-c("0"=1); s<-0; c<-0; for(x in n){ s<-s+x; key<-as.character(s-k); if(!is.na(m[key])) c<-c+m[key]; ks<-as.character(s); m[ks]<-ifelse(is.na(m[ks]),1,m[ks]+1) }; c }
cat(subarraySum(c(1,1,1),2),"\n")
