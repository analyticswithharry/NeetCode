# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 233 -- Merge K Sorted Lists
# Category   : Linked List
# Difficulty : Hard
# Study Plan : Day 117
# =============================================================
#
# QUESTION:
#   Merge K sorted linked lists into one. Use heap.
# =============================================================
import heapq
class N:
    def __init__(s,v,n=None): s.v=v; s.n=n
def mergeK(lists):
    h=[]
    for i,L in enumerate(lists):
        if L: heapq.heappush(h,(L.v,i,L))
    d=N(0); cur=d; ctr=len(lists)
    while h:
        v,_,nd=heapq.heappop(h); cur.n=nd; cur=nd
        if nd.n: ctr+=1; heapq.heappush(h,(nd.n.v,ctr,nd.n))
    return d.n
def to(a):
    d=N(0); c=d
    for x in a: c.n=N(x); c=c.n
    return d.n
def out(h):
    r=[]
    while h: r.append(h.v); h=h.n
    return r
if __name__=="__main__":
    print(out(mergeK([to([1,4,5]),to([1,3,4]),to([2,6])])))
