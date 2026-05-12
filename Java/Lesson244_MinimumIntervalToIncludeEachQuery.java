// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 244 -- Minimum Interval to Include Each Query
// Category   : Intervals
// Difficulty : Hard
// Study Plan : Day 122
// =============================================================
//
// QUESTION:
//   For each query q, find smallest interval covering q.
// =============================================================
import java.util.*;
public class Lesson244_MinimumIntervalToIncludeEachQuery{
  static int[] minInterval(int[][] iv,int[] q){Arrays.sort(iv,(a,b)->a[0]-b[0]);Integer[] idx=new Integer[q.length];for(int i=0;i<q.length;i++)idx[i]=i;Arrays.sort(idx,(a,b)->q[a]-q[b]);int[] res=new int[q.length];PriorityQueue<int[]> h=new PriorityQueue<>((a,b)->a[0]-b[0]);int i=0;for(int k:idx){int v=q[k];while(i<iv.length&&iv[i][0]<=v){h.add(new int[]{iv[i][1]-iv[i][0]+1,iv[i][1]});i++;}while(!h.isEmpty()&&h.peek()[1]<v)h.poll();res[k]=h.isEmpty()?-1:h.peek()[0];}return res;}
  public static void main(String[]a){System.out.println(Arrays.toString(minInterval(new int[][]{{1,4},{2,4},{3,6},{4,4}},new int[]{2,3,4,5})));}
}
