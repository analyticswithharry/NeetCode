# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 118 -- Meeting Rooms III
# Category   : Intervals
# Difficulty : Hard
# Study Plan : Day 59
# =============================================================
#
# QUESTION:
#   Given n rooms (0..n-1) and meetings [start,end], assign meetings to lowest-numbered available room, delaying if needed (preserving duration). Return room hosting most meetings.
# =============================================================
mostBooked <- function(n,m){ m <- m[order(sapply(m,`[`,1))]; fr <- 0:(n-1); busy <- list(); cnt <- rep(0,n); for(x in m){ keep<-c(); for(i in seq_along(busy)){ if(busy[[i]][1]<=x[1]){ fr<-c(fr,busy[[i]][2]) } else keep<-c(keep,i) }; busy<-busy[keep]; if(length(fr)>0){ r<-min(fr); fr<-fr[fr!=r]; e<-x[2] } else { ts<-sapply(busy,`[`,1); k<-which.min(ts); r<-busy[[k]][2]; e<-busy[[k]][1]+x[2]-x[1]; busy<-busy[-k] }; busy[[length(busy)+1]] <- c(e,r); cnt[r+1]<-cnt[r+1]+1 }; which.max(cnt)-1 }
cat(mostBooked(2,list(c(0,10),c(1,5),c(2,7),c(3,4))),"\n")
