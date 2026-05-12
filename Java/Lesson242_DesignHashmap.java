// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 242 -- Design HashMap
// Category   : Arrays and Hashing
// Difficulty : Easy
// Study Plan : Day 121
// =============================================================
//
// QUESTION:
//   Implement HashMap with put/get/remove using bucket separate chaining.
// =============================================================
import java.util.*;
public class Lesson242_DesignHashmap{
  static class HM{int B=997;List<int[]>[] b=new List[B];HM(){for(int i=0;i<B;i++)b[i]=new ArrayList<>();}int h(int k){return ((k%B)+B)%B;}void put(int k,int v){List<int[]> x=b[h(k)];for(int[] p:x)if(p[0]==k){p[1]=v;return;}x.add(new int[]{k,v});}int get(int k){for(int[] p:b[h(k)])if(p[0]==k)return p[1];return -1;}void remove(int k){List<int[]> x=b[h(k)];for(int i=0;i<x.size();i++)if(x.get(i)[0]==k){x.remove(i);return;}}}
  public static void main(String[]a){HM m=new HM();m.put(1,1);m.put(2,2);System.out.println(m.get(1)+" "+m.get(3));m.remove(1);System.out.println(m.get(1));}
}
