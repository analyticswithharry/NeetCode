# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 228 -- LFU Cache
# Category   : Linked List
# Difficulty : Hard
# Study Plan : Day 114
# =============================================================
#
# QUESTION:
#   LFU eviction; tie-break by least recently used. Use freq buckets of OrderedDict.
# =============================================================
from collections import defaultdict, OrderedDict
class LFU:
    def __init__(s,c): s.c=c; s.k={}; s.f=defaultdict(OrderedDict); s.mn=0
    def _bump(s,k):
        f=s.k[k][1]; v=s.f[f].pop(k)
        if not s.f[f] and s.mn==f: s.mn+=1
        s.f[f+1][k]=v; s.k[k]=(v,f+1)
    def get(s,k):
        if k not in s.k: return -1
        s._bump(k); return s.k[k][0]
    def put(s,k,v):
        if s.c==0: return
        if k in s.k: s.k[k]=(v,s.k[k][1]); s.f[s.k[k][1]][k]=v; s._bump(k); return
        if len(s.k)>=s.c:
            ek,_=s.f[s.mn].popitem(last=False); del s.k[ek]
        s.k[k]=(v,1); s.f[1][k]=v; s.mn=1
if __name__=="__main__":
    c=LFU(2); c.put(1,1); c.put(2,2); print(c.get(1)); c.put(3,3); print(c.get(2))
