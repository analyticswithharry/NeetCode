# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 129 -- Maximum Sum Circular Subarray
# Category   : Greedy
# Difficulty : Medium
# Study Plan : Day 65
# =============================================================
#
# QUESTION:
#   Given a circular integer array, find the maximum subarray sum (subarray may wrap).
# =============================================================
maxCirc <- function(a){ tot<-0; mxc<-a[1]; cur<-a[1]; mnc<-a[1]; c2<-a[1]; for(i in seq_along(a)){ if(i>1){ cur<-max(a[i],cur+a[i]); mxc<-max(mxc,cur); c2<-min(a[i],c2+a[i]); mnc<-min(mnc,c2) }; tot<-tot+a[i] }; if(mxc<0) mxc else max(mxc,tot-mnc) }
cat(maxCirc(c(1,-2,3,-2)),"\n"); cat(maxCirc(c(5,-3,5)),"\n"); cat(maxCirc(c(-3,-2,-3)),"\n")
