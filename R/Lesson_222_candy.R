# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 222 -- Candy
# Category   : Greedy
# Difficulty : Hard
# Study Plan : Day 111
# =============================================================
#
# QUESTION:
#   Each child gets >=1 candy; higher rating gets more than neighbors. Return min candies.
# =============================================================
candy <- function(r){ n<-length(r); a<-rep(1,n); for(i in 2:n) if(r[i]>r[i-1]) a[i]<-a[i-1]+1; for(i in (n-1):1) if(r[i]>r[i+1] && a[i]<=a[i+1]) a[i]<-a[i+1]+1; sum(a) }
cat(candy(c(1,0,2)),"\n")
