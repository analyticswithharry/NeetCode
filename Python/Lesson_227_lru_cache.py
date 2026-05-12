# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 227 -- LRU Cache
# Category   : Linked List
# Difficulty : Medium
# Study Plan : Day 114
# =============================================================
#
# QUESTION:
#   Design LRU cache with O(1) get and put.
# =============================================================
from collections import OrderedDict
class LRU:
    def __init__(s,c): s.c=c; s.d=OrderedDict()
    def get(s,k):
        if k not in s.d: return -1
        s.d.move_to_end(k); return s.d[k]
    def put(s,k,v):
        if k in s.d: s.d.move_to_end(k)
        s.d[k]=v
        if len(s.d)>s.c: s.d.popitem(last=False)
if __name__=="__main__":
    c=LRU(2); c.put(1,1); c.put(2,2); print(c.get(1)); c.put(3,3); print(c.get(2))
