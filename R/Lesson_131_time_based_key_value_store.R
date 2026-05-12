# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 131 -- Time Based Key Value Store
# Category   : Binary Search
# Difficulty : Medium
# Study Plan : Day 66
# =============================================================
#
# QUESTION:
#   Design TimeMap: set(k,v,t) and get(k,t) returns value with greatest timestamp <= t.
# =============================================================
TimeMap <- function(){ env<-new.env(hash=TRUE); list(set=function(k,v,t){ x<-if(exists(k,envir=env)) get(k,envir=env) else list(t=c(),v=c()); x$t<-c(x$t,t); x$v<-c(x$v,v); assign(k,x,envir=env) }, get=function(k,t){ if(!exists(k,envir=env)) return(""); x<-get(k,envir=env); idx<-max(c(0,which(x$t<=t))); if(idx==0) "" else x$v[idx] }) }
tm<-TimeMap(); tm$set("foo","bar",1); cat(tm$get("foo",1),"\n"); cat(tm$get("foo",3),"\n"); tm$set("foo","bar2",4); cat(tm$get("foo",4),"\n"); cat(tm$get("foo",5),"\n")
