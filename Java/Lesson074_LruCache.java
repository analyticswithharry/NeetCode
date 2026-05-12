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

import java.util.*;
public class Lesson074_LruCache {
    static class LRU extends LinkedHashMap<Integer,Integer> {
        private final int cap;
        LRU(int c){ super(c, 0.75f, true); this.cap = c; }
        protected boolean removeEldestEntry(Map.Entry<Integer,Integer> e){ return size() > cap; }
    }
    public static void main(String[] a){
        LRU c = new LRU(2); c.put(1,1); c.put(2,2);
        System.out.println(c.getOrDefault(1,-1));
        c.put(3,3); System.out.println(c.getOrDefault(2,-1));
        c.put(4,4); System.out.println(c.getOrDefault(1,-1)+" "+c.getOrDefault(3,-1)+" "+c.getOrDefault(4,-1));
    }
}
