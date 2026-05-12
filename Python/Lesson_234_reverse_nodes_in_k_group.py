# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 234 -- Reverse Nodes In K Group
# Category   : Linked List
# Difficulty : Hard
# Study Plan : Day 117
# =============================================================
#
# QUESTION:
#   Reverse nodes in groups of k. Remaining tail stays.
# =============================================================
class N:
    def __init__(s,v,n=None): s.v=v; s.n=n
def reverseK(head,k):
    d=N(0,head); g=d
    while True:
        kth=g
        for _ in range(k):
            kth=kth.n
            if not kth: return d.n
        nxt=kth.n; pre,cur=nxt,g.n
        while cur is not nxt:
            tmp=cur.n; cur.n=pre; pre=cur; cur=tmp
        tmp=g.n; g.n=kth; g=tmp
def to(a):
    d=N(0); c=d
    for x in a: c.n=N(x); c=c.n
    return d.n
def out(h):
    r=[]
    while h: r.append(h.v); h=h.n
    return r
if __name__=="__main__":
    print(out(reverseK(to([1,2,3,4,5]),2)))
