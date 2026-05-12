# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 160 -- IPO
# Category   : Heap Priority Queue
# Difficulty : Hard
# Study Plan : Day 80
# =============================================================
#
# QUESTION:
#   Pick at most k projects with capital >= w each. Each project gives profit; w grows. Maximize final w.
# =============================================================
import heapq
def ipo(k,w,profits,capital):
    proj=sorted(zip(capital,profits)); h=[]; i=0; n=len(profits)
    for _ in range(k):
        while i<n and proj[i][0]<=w: heapq.heappush(h,-proj[i][1]); i+=1
        if not h: break
        w-=heapq.heappop(h)
    return w

if __name__=="__main__":
    print(ipo(2,0,[1,2,3],[0,1,1]))
    print(ipo(3,0,[1,2,3],[0,1,2]))
