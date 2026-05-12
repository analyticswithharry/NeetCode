# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 246 -- Largest Rectangle In Histogram
# Category   : Stack
# Difficulty : Hard
# Study Plan : Day 123
# =============================================================
#
# QUESTION:
#   Max rectangular area in histogram. Monotonic stack.
# =============================================================
largestRect <- function(h){ h<-c(h,0); st<-c(); best<-0; for(i in seq_along(h)){ while(length(st)>0 && h[st[length(st)]]>h[i]){ top<-st[length(st)]; st<-st[-length(st)]; w<-if(length(st)==0) i-1 else i-st[length(st)]-1; best<-max(best,h[top]*w) }; st<-c(st,i) }; best }
cat(largestRect(c(2,1,5,6,2,3)),"\n")
