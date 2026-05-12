// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 131 -- Time Based Key Value Store
// Category   : Binary Search
// Difficulty : Medium
// Study Plan : Day 66
// =============================================================
//
// QUESTION:
//   Design TimeMap: set(k,v,t) and get(k,t) returns value with greatest timestamp <= t.
// =============================================================
import java.util.*;
public class Lesson131_TimeBasedKeyValueStore{
  static class TimeMap{Map<String,List<int[]>> mt=new HashMap<>();Map<String,List<String>> mv=new HashMap<>();void set(String k,String v,int t){mt.computeIfAbsent(k,x->new ArrayList<>()).add(new int[]{t});mv.computeIfAbsent(k,x->new ArrayList<>()).add(v);}String get(String k,int t){if(!mt.containsKey(k))return "";var ts=mt.get(k);var vs=mv.get(k);int lo=0,hi=ts.size()-1,r=-1;while(lo<=hi){int m=(lo+hi)>>>1;if(ts.get(m)[0]<=t){r=m;lo=m+1;}else hi=m-1;}return r<0?"":vs.get(r);}}
  public static void main(String[]x){TimeMap tm=new TimeMap();tm.set("foo","bar",1);System.out.println(tm.get("foo",1));System.out.println(tm.get("foo",3));tm.set("foo","bar2",4);System.out.println(tm.get("foo",4));System.out.println(tm.get("foo",5));}
}
