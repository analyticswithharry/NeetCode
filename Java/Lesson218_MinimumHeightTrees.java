// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 218 -- Minimum Height Trees
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 109
// =============================================================
//
// QUESTION:
//   Given an undirected tree, find roots that produce minimum-height trees (peel leaves BFS).
// =============================================================
import java.util.*;
public class Lesson218_MinimumHeightTrees{
  static List<Integer> findMHT(int n,int[][] e){if(n==1)return Arrays.asList(0);Set<Integer>[] g=new HashSet[n];for(int i=0;i<n;i++)g[i]=new HashSet<>();int[] d=new int[n];for(int[] x:e){g[x[0]].add(x[1]);g[x[1]].add(x[0]);d[x[0]]++;d[x[1]]++;}Deque<Integer> q=new ArrayDeque<>();for(int i=0;i<n;i++)if(d[i]==1)q.add(i);int rem=n;while(rem>2){int sz=q.size();rem-=sz;for(int i=0;i<sz;i++){int x=q.poll();for(int y:g[x]){d[y]--;if(d[y]==1)q.add(y);}}}return new ArrayList<>(q);}
  public static void main(String[]a){System.out.println(findMHT(6,new int[][]{{3,0},{3,1},{3,2},{3,4},{5,4}}));}
}
