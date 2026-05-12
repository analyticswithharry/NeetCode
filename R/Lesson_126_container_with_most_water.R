# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 126 -- Container With Most Water
# Category   : Two Pointers
# Difficulty : Medium
# Study Plan : Day 63
# =============================================================
#
# QUESTION:
#   Given heights, find two lines that form the container holding most water.
# =============================================================
maxArea <- function(h){ l<-1; r<-length(h); b<-0; while(l<r){ b<-max(b,(r-l)*min(h[l],h[r])); if(h[l]<h[r]) l<-l+1 else r<-r-1 }; b }
cat(maxArea(c(1,8,6,2,5,4,8,3,7)),"\n")
