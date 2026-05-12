// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 228 -- LFU Cache
// Category   : Linked List
// Difficulty : Hard
// Study Plan : Day 114
// =============================================================
//
// QUESTION:
//   LFU eviction; tie-break by least recently used. Use freq buckets of OrderedDict.
// =============================================================
import java.util.*;
public class Lesson228_LfuCache{
  static class LFU{int c,mn;Map<Integer,int[]> k=new HashMap<>();Map<Integer,LinkedHashMap<Integer,Integer>> f=new HashMap<>();LFU(int c){this.c=c;}LinkedHashMap<Integer,Integer> b(int x){return f.computeIfAbsent(x,z->new LinkedHashMap<>());}void bump(int x){int[] p=k.get(x);b(p[1]).remove(x);if(b(p[1]).isEmpty()&&mn==p[1])mn++;p[1]++;b(p[1]).put(x,p[0]);}int get(int x){if(!k.containsKey(x))return -1;bump(x);return k.get(x)[0];}void put(int x,int v){if(c==0)return;if(k.containsKey(x)){k.get(x)[0]=v;b(k.get(x)[1]).put(x,v);bump(x);return;}if(k.size()>=c){int ek=b(mn).keySet().iterator().next();b(mn).remove(ek);k.remove(ek);}k.put(x,new int[]{v,1});b(1).put(x,v);mn=1;}}
  public static void main(String[]a){LFU c=new LFU(2);c.put(1,1);c.put(2,2);System.out.println(c.get(1));c.put(3,3);System.out.println(c.get(2));}
}
