# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 242 -- Design HashMap
# Category   : Arrays and Hashing
# Difficulty : Easy
# Study Plan : Day 121
# =============================================================
#
# QUESTION:
#   Implement HashMap with put/get/remove using bucket separate chaining.
# =============================================================
class HM:
    def __init__(s): s.B=997; s.b=[[] for _ in range(s.B)]
    def _h(s,k): return k%s.B
    def put(s,k,v):
        b=s.b[s._h(k)]
        for i,(kk,_) in enumerate(b):
            if kk==k: b[i]=(k,v); return
        b.append((k,v))
    def get(s,k):
        for kk,vv in s.b[s._h(k)]:
            if kk==k: return vv
        return -1
    def remove(s,k):
        b=s.b[s._h(k)]
        for i,(kk,_) in enumerate(b):
            if kk==k: b.pop(i); return
if __name__=="__main__":
    m=HM(); m.put(1,1); m.put(2,2); print(m.get(1),m.get(3)); m.remove(1); print(m.get(1))
