// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 074 -- LRU Cache
// Category   : Linked List
// Difficulty : Medium
// Study Plan : Day 37
// =============================================================
//
// QUESTION:
//   Design an LRU cache with O(1) get and put.
// =============================================================

class LRUCache {
    constructor(cap){ this.cap = cap; this.m = new Map(); }
    get(k){ if (!this.m.has(k)) return -1; const v = this.m.get(k); this.m.delete(k); this.m.set(k,v); return v; }
    put(k, v){ if (this.m.has(k)) this.m.delete(k); this.m.set(k,v); if (this.m.size > this.cap) this.m.delete(this.m.keys().next().value); }
}
const c = new LRUCache(2); c.put(1,1); c.put(2,2); console.log(c.get(1));
c.put(3,3); console.log(c.get(2)); c.put(4,4); console.log(c.get(1), c.get(3), c.get(4));
