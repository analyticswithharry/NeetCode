# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 074 -- LRU Cache
# Category   : Linked List
# Difficulty : Medium
# Study Plan : Day 37
# =============================================================
#
# QUESTION:
#   Design an LRU cache with O(1) get and put.
# =============================================================

from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity): self.cap = capacity; self.d = OrderedDict()
    def get(self, key):
        if key not in self.d: return -1
        self.d.move_to_end(key); return self.d[key]
    def put(self, key, value):
        if key in self.d: self.d.move_to_end(key)
        self.d[key] = value
        if len(self.d) > self.cap: self.d.popitem(last=False)

if __name__ == "__main__":
    c = LRUCache(2); c.put(1,1); c.put(2,2); print(c.get(1))
    c.put(3,3); print(c.get(2)); c.put(4,4); print(c.get(1), c.get(3), c.get(4))
