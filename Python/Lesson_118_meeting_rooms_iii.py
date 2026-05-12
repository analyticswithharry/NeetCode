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
import heapq
def mostBooked(n, meets):
    meets.sort()
    free=list(range(n))
    heapq.heapify(free)
    busy=[]  # (endTime, room)
    cnt=[0]*n
    for s,e in meets:
        while busy and busy[0][0]<=s:
            _,r=heapq.heappop(busy); heapq.heappush(free,r)
        if free:
            r=heapq.heappop(free)
            heapq.heappush(busy,(e,r))
        else:
            t,r=heapq.heappop(busy)
            heapq.heappush(busy,(t+e-s,r))
        cnt[r]+=1
    return cnt.index(max(cnt))

if __name__=="__main__":
    print(mostBooked(2,[[0,10],[1,5],[2,7],[3,4]]))
