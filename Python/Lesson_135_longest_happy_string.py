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
import heapq
def longest(a,b,c):
    h=[]
    for cnt,ch in [(-a,'a'),(-b,'b'),(-c,'c')]:
        if cnt: heapq.heappush(h,(cnt,ch))
    out=[]
    while h:
        c1,ch1=heapq.heappop(h)
        if len(out)>=2 and out[-1]==out[-2]==ch1:
            if not h: break
            c2,ch2=heapq.heappop(h)
            out.append(ch2); c2+=1
            if c2: heapq.heappush(h,(c2,ch2))
            heapq.heappush(h,(c1,ch1))
        else:
            out.append(ch1); c1+=1
            if c1: heapq.heappush(h,(c1,ch1))
    return "".join(out)

if __name__=="__main__":
    print(longest(1,1,7))
    print(longest(7,1,0))
