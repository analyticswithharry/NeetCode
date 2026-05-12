# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 216 -- Partition Labels
# Category   : Greedy
# Difficulty : Medium
# Study Plan : Day 108
# =============================================================
#
# QUESTION:
#   Partition string so each char appears in at most one part. Return sizes.
# =============================================================
partitionLabels <- function(s){ v<-strsplit(s,"")[[1]]; last<-sapply(unique(v),function(c) max(which(v==c))); r<-c(); st<-1; e<-0; for(i in seq_along(v)){ e<-max(e,last[v[i]]); if(i==e){ r<-c(r,e-st+1); st<-i+1 } }; r }
cat(partitionLabels("ababcbacadefegdehijhklij"),"\n")
