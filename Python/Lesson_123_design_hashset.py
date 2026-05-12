# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 123 -- Design HashSet
# Category   : Arrays and Hashing
# Difficulty : Easy
# Study Plan : Day 62
# =============================================================
#
# QUESTION:
#   Design a HashSet (without built-in set): add, remove, contains.
# =============================================================
class MyHashSet:
    def __init__(self): self.b=[[] for _ in range(769)]
    def _h(self,k): return k%769
    def add(self,k):
        b=self.b[self._h(k)]
        if k not in b: b.append(k)
    def remove(self,k):
        b=self.b[self._h(k)]
        if k in b: b.remove(k)
    def contains(self,k): return k in self.b[self._h(k)]

if __name__=="__main__":
    s=MyHashSet(); s.add(1); s.add(2); print(s.contains(1), s.contains(3)); s.remove(2); print(s.contains(2))
