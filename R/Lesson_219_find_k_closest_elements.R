# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 219 -- Find K Closest Elements
# Category   : Sliding Window
# Difficulty : Medium
# Study Plan : Day 110
# =============================================================
#
# QUESTION:
#   Return k closest sorted ints to x (binary search the window).
# =============================================================
findClosest <- function(a,k,x){ l<-1; r<-length(a)-k+1; while(l<r){ m<-(l+r)%/%2; if(x-a[m]>a[m+k]-x) l<-m+1 else r<-m }; a[l:(l+k-1)] }
cat(findClosest(c(1,2,3,4,5),4,3),"\n")
