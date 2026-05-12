# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 114 -- Search In Rotated Sorted Array II
# Category   : Binary Search
# Difficulty : Medium
# Study Plan : Day 57
# =============================================================
#
# QUESTION:
#   Rotated sorted array may contain duplicates. Return true if target exists.
# =============================================================
search <- function(a,t){ lo<-1;hi<-length(a); while(lo<=hi){ m<-(lo+hi)%/%2; if(a[m]==t) return(TRUE); if(a[lo]==a[m] && a[m]==a[hi]){ lo<-lo+1; hi<-hi-1 } else if(a[lo]<=a[m]){ if(a[lo]<=t && t<a[m]) hi<-m-1 else lo<-m+1 } else { if(a[m]<t && t<=a[hi]) lo<-m+1 else hi<-m-1 } }; FALSE }
cat(search(c(2,5,6,0,0,1,2),0),"\n"); cat(search(c(2,5,6,0,0,1,2),3),"\n")
