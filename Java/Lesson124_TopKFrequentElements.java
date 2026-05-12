// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 124 -- Top K Frequent Elements
// Category   : Arrays and Hashing
// Difficulty : Medium
// Study Plan : Day 62
// =============================================================
//
// QUESTION:
//   Given an integer array nums and integer k, return the k most frequent elements.
// =============================================================
import java.util.*;
public class Lesson124_TopKFrequentElements{
  static int[] topK(int[]a,int k){Map<Integer,Integer> m=new HashMap<>();for(int x:a)m.merge(x,1,Integer::sum);List<Map.Entry<Integer,Integer>> e=new ArrayList<>(m.entrySet());e.sort((p,q)->q.getValue()-p.getValue());int[] r=new int[k];for(int i=0;i<k;i++)r[i]=e.get(i).getKey();return r;}
  public static void main(String[]x){System.out.println(Arrays.toString(topK(new int[]{1,1,1,2,2,3},2)));}
}
