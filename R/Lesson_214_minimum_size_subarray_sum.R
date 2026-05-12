# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 214 -- Minimum Size Subarray Sum
# Category   : Sliding Window
# Difficulty : Medium
# Study Plan : Day 107
# =============================================================
#
# QUESTION:
#   Return the minimum length of a contiguous subarray whose sum is >= target. 0 if none.
# =============================================================
minSubArrayLen <- function(t,n){ l<-1; s<-0; ans<-Inf; for(r in seq_along(n)){ s<-s+n[r]; while(s>=t){ ans<-min(ans,r-l+1); s<-s-n[l]; l<-l+1 } }; if(is.infinite(ans)) 0 else ans }
cat(minSubArrayLen(7,c(2,3,1,2,4,3)),"\n")
