// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 240 -- Subarray Sum Equals K
// Category   : Arrays and Hashing
// Difficulty : Medium
// Study Plan : Day 120
// =============================================================
//
// QUESTION:
//   Count subarrays with sum k using prefix-sum frequency map.
// =============================================================
import java.util.*;
public class Lesson240_SubarraySumEqualsK{
  static int subarraySum(int[] n,int k){Map<Integer,Integer> m=new HashMap<>();m.put(0,1);int s=0,c=0;for(int x:n){s+=x;c+=m.getOrDefault(s-k,0);m.merge(s,1,Integer::sum);}return c;}
  public static void main(String[]a){System.out.println(subarraySum(new int[]{1,1,1},2));}
}
