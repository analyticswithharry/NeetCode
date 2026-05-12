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
import heapq
def minRooms(it):
    it.sort(key=lambda x:x[0]); h=[]
    for s,e in it:
        if h and h[0]<=s: heapq.heappop(h)
        heapq.heappush(h,e)
    return len(h)

if __name__=="__main__":
    print(minRooms([[0,30],[5,10],[15,20]]))
    print(minRooms([[7,10],[2,4]]))
