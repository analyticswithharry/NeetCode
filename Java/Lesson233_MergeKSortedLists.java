// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 233 -- Merge K Sorted Lists
// Category   : Linked List
// Difficulty : Hard
// Study Plan : Day 117
// =============================================================
//
// QUESTION:
//   Merge K sorted linked lists into one. Use heap.
// =============================================================
import java.util.*;
public class Lesson233_MergeKSortedLists{
  static class N{int v;N n;N(int v){this.v=v;}}
  static N mergeK(List<N> lists){PriorityQueue<int[]> q=new PriorityQueue<>((a,b)->a[0]-b[0]);for(int i=0;i<lists.size();i++)if(lists.get(i)!=null)q.add(new int[]{lists.get(i).v,i});List<N> heads=new ArrayList<>(lists);N d=new N(0),c=d;while(!q.isEmpty()){int[] t=q.poll();c.n=new N(t[0]);c=c.n;heads.set(t[1],heads.get(t[1]).n);if(heads.get(t[1])!=null)q.add(new int[]{heads.get(t[1]).v,t[1]});}return d.n;}
  static N to(int[] a){N d=new N(0),c=d;for(int x:a){c.n=new N(x);c=c.n;}return d.n;}
  public static void main(String[]a){List<N> L=Arrays.asList(to(new int[]{1,4,5}),to(new int[]{1,3,4}),to(new int[]{2,6}));N r=mergeK(L);while(r!=null){System.out.print(r.v+" ");r=r.n;}System.out.println();}
}
