# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 160 -- IPO
# Category   : Heap Priority Queue
# Difficulty : Hard
# Study Plan : Day 80
# =============================================================
#
# QUESTION:
#   Pick at most k projects with capital >= w each. Each project gives profit; w grows. Maximize final w.
# =============================================================
ipo <- function(k,w,profits,capital){ n<-length(profits); ord<-order(capital); cap<-capital[ord]; pr<-profits[ord]; h<-c(); i<-1; for(s in 1:k){ while(i<=n && cap[i]<=w){ h<-c(h,pr[i]); i<-i+1 }; if(length(h)==0) break; idx<-which.max(h); w<-w+h[idx]; h<-h[-idx] }; w }
cat(ipo(2,0,c(1,2,3),c(0,1,1)),"\n"); cat(ipo(3,0,c(1,2,3),c(0,1,2)),"\n")
