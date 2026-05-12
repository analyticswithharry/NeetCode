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
import java.util.*;
public class Lesson227_LruCache{
  static class LRU extends LinkedHashMap<Integer,Integer>{int c;LRU(int c){super(16,0.75f,true);this.c=c;}protected boolean removeEldestEntry(Map.Entry<Integer,Integer> e){return size()>c;}int g(int k){return getOrDefault(k,-1);}}
  public static void main(String[]a){LRU c=new LRU(2);c.put(1,1);c.put(2,2);System.out.println(c.g(1));c.put(3,3);System.out.println(c.g(2));}
}
