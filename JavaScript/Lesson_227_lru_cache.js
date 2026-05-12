// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 227 -- LRU Cache
// Category   : Linked List
// Difficulty : Medium
// Study Plan : Day 114
// =============================================================
//
// QUESTION:
//   Design LRU cache with O(1) get and put.
// =============================================================
class LRU{constructor(c){this.c=c;this.m=new Map();}get(k){if(!this.m.has(k))return -1;const v=this.m.get(k);this.m.delete(k);this.m.set(k,v);return v;}put(k,v){if(this.m.has(k))this.m.delete(k);this.m.set(k,v);if(this.m.size>this.c)this.m.delete(this.m.keys().next().value);}}
const c=new LRU(2);c.put(1,1);c.put(2,2);console.log(c.get(1));c.put(3,3);console.log(c.get(2));
