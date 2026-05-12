# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 149 -- Daily Temperatures
# Category   : Stack
# Difficulty : Medium
# Study Plan : Day 75
# =============================================================
#
# QUESTION:
#   For each day, return number of days until a warmer temperature, or 0.
# =============================================================
dailyT <- function(t){ r<-rep(0,length(t)); st<-c(); for(i in seq_along(t)){ while(length(st)>0 && t[st[length(st)]]<t[i]){ j<-st[length(st)]; st<-st[-length(st)]; r[j]<-i-j }; st<-c(st,i) }; r }
print(dailyT(c(73,74,75,71,69,72,76,73)))
