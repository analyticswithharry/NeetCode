# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 125 -- Merge Sorted Array
# Category   : Two Pointers
# Difficulty : Easy
# Study Plan : Day 63
# =============================================================
#
# QUESTION:
#   Given nums1 (length m+n) and nums2 (length n) sorted, merge nums2 into nums1 in-place sorted.
# =============================================================
merge2 <- function(a,m,b,n){ i<-m;j<-n;k<-m+n; while(j>=1){ if(i>=1 && a[i]>b[j]){ a[k]<-a[i]; i<-i-1 } else { a[k]<-b[j]; j<-j-1 }; k<-k-1 }; a }
print(merge2(c(1,2,3,0,0,0),3,c(2,5,6),3))
