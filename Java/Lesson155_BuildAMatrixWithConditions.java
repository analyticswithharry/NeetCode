// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 155 -- Build a Matrix With Conditions
// Category   : Advanced Graphs
// Difficulty : Hard
// Study Plan : Day 78
// =============================================================
//
// QUESTION:
//   Given k rows/cols and conditions for row/col orderings, place 1..k so each appears once and conditions are satisfied. Return matrix or [].
// =============================================================
import java.util.*;
public class Lesson155_BuildAMatrixWithConditions{
  static int[] topo(int k,int[][] conds){List<List<Integer>> adj=new ArrayList<>();for(int i=0;i<=k;i++)adj.add(new ArrayList<>());int[] ind=new int[k+1];for(int[] c:conds){adj.get(c[0]).add(c[1]);ind[c[1]]++;}Queue<Integer> q=new ArrayDeque<>();for(int i=1;i<=k;i++)if(ind[i]==0)q.add(i);int[] o=new int[k];int idx=0;while(!q.isEmpty()){int x=q.poll();o[idx++]=x;for(int y:adj.get(x))if(--ind[y]==0)q.add(y);}return idx==k?o:new int[0];}
  static int[][] build(int k,int[][] rC,int[][] cC){int[] r=topo(k,rC),c=topo(k,cC);if(r.length==0||c.length==0)return new int[0][0];int[] pos=new int[k+1];for(int i=0;i<k;i++)pos[c[i]]=i;int[][] g=new int[k][k];for(int i=0;i<k;i++)g[i][pos[r[i]]]=r[i];return g;}
  public static void main(String[]x){System.out.println(Arrays.deepToString(build(3,new int[][]{{1,2},{3,2}},new int[][]{{2,1},{3,2}})));}
}
