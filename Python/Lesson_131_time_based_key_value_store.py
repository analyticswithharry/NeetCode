# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 131 -- Time Based Key Value Store
# Category   : Binary Search
# Difficulty : Medium
# Study Plan : Day 66
# =============================================================
#
# QUESTION:
#   Design TimeMap: set(k,v,t) and get(k,t) returns value with greatest timestamp <= t.
# =============================================================
import bisect
class TimeMap:
    def __init__(self): self.m={}
    def set(self,k,v,t): self.m.setdefault(k,([],[]))[0].append(t); self.m[k][1].append(v)
    def get(self,k,t):
        if k not in self.m: return ""
        ts,vs=self.m[k]
        i=bisect.bisect_right(ts,t)-1
        return vs[i] if i>=0 else ""

if __name__=="__main__":
    tm=TimeMap(); tm.set("foo","bar",1); print(tm.get("foo",1)); print(tm.get("foo",3)); tm.set("foo","bar2",4); print(tm.get("foo",4)); print(tm.get("foo",5))
