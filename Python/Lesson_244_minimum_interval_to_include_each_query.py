# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 244 -- Minimum Interval to Include Each Query
# Category   : Intervals
# Difficulty : Hard
# Study Plan : Day 122
# =============================================================
#
# QUESTION:
#   For each query q, find smallest interval covering q.
# =============================================================
import heapq
def minInterval(intervals,queries):
    intervals.sort()
    res={}; h=[]; i=0
    for q in sorted(queries):
        while i<len(intervals) and intervals[i][0]<=q:
            l,r=intervals[i]; heapq.heappush(h,(r-l+1,r)); i+=1
        while h and h[0][1]<q: heapq.heappop(h)
        res[q]=h[0][0] if h else -1
    return [res[q] for q in queries]
if __name__=="__main__":
    print(minInterval([[1,4],[2,4],[3,6],[4,4]],[2,3,4,5]))
