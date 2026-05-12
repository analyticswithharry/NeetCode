// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 123 -- Design HashSet
// Category   : Arrays and Hashing
// Difficulty : Easy
// Study Plan : Day 62
// =============================================================
//
// QUESTION:
//   Design a HashSet (without built-in set): add, remove, contains.
// =============================================================
import java.util.*;
public class Lesson123_DesignHashset{
  static class MyHashSet{List<List<Integer>> b=new ArrayList<>();MyHashSet(){for(int i=0;i<769;i++)b.add(new ArrayList<>());}int h(int k){return k%769;}void add(int k){var x=b.get(h(k));if(!x.contains(k))x.add(k);}void remove(int k){b.get(h(k)).remove(Integer.valueOf(k));}boolean contains(int k){return b.get(h(k)).contains(k);}}
  public static void main(String[]x){MyHashSet s=new MyHashSet();s.add(1);s.add(2);System.out.println(s.contains(1)+" "+s.contains(3));s.remove(2);System.out.println(s.contains(2));}
}
