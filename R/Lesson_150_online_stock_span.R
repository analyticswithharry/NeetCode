# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 150 -- Online Stock Span
# Category   : Stack
# Difficulty : Medium
# Study Plan : Day 75
# =============================================================
#
# QUESTION:
#   Implement StockSpanner.next(price): consecutive days <= today's price (including today).
# =============================================================
StockSpanner <- function(){ st<-list(); next_ <- function(p){ s<-1; while(length(st)>0 && st[[length(st)]][1]<=p){ s<-s+st[[length(st)]][2]; st[[length(st)]]<<-NULL }; st[[length(st)+1]]<<-c(p,s); s }; list(next_=next_) }
s<-StockSpanner(); print(sapply(c(100,80,60,70,60,75,85),s$next_))
