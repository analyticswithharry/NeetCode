# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 117 -- Meeting Rooms II
# Category   : Intervals
# Difficulty : Medium
# Study Plan : Day 59
# =============================================================
#
# QUESTION:
#   Given an array of meeting time intervals, return the minimum number of conference rooms required.
# =============================================================
minRooms <- function(it){ it <- it[order(sapply(it,`[`,1))]; h<-c(); for(x in it){ if(length(h)>0 && min(h)<=x[1]){ h<-h[-which.min(h)] }; h<-c(h,x[2]) }; length(h) }
cat(minRooms(list(c(0,30),c(5,10),c(15,20))),"\n"); cat(minRooms(list(c(7,10),c(2,4))),"\n")
