# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 135 -- Longest Happy String
# Category   : Heap Priority Queue
# Difficulty : Medium
# Study Plan : Day 68
# =============================================================
#
# QUESTION:
#   Given a,b,c counts of letters, build the longest string with at most a 'a', b 'b', c 'c' such that no three consecutive letters are equal.
# =============================================================
longest <- function(a,b,c){ h<-list(); if(a>0) h[[length(h)+1]]<-c(a,utf8ToInt('a')); if(b>0) h[[length(h)+1]]<-c(b,utf8ToInt('b')); if(c>0) h[[length(h)+1]]<-c(c,utf8ToInt('c')); s<-c(); popMax<-function(){ idx<-which.max(sapply(h,`[`,1)); x<-h[[idx]]; h[[idx]]<<-NULL; x }; while(length(h)>0){ x<-popMax(); n<-length(s); if(n>=2 && s[n]==x[2] && s[n-1]==x[2]){ if(length(h)==0) break; y<-popMax(); s<-c(s,y[2]); if(y[1]-1>0) h[[length(h)+1]]<-c(y[1]-1,y[2]); h[[length(h)+1]]<-x } else { s<-c(s,x[2]); if(x[1]-1>0) h[[length(h)+1]]<-c(x[1]-1,x[2]) } }; intToUtf8(s) }
cat(longest(1,1,7),"\n"); cat(longest(7,1,0),"\n")
