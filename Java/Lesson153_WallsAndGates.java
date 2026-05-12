// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 153 -- Walls And Gates
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 77
// =============================================================
//
// QUESTION:
//   Grid: -1 wall, 0 gate, INF empty. Fill each empty with distance to nearest gate.
// =============================================================
import java.util.*;
public class Lesson153_WallsAndGates{
  static final int INF=Integer.MAX_VALUE;
  static int[][] walls(int[][]g){if(g.length==0)return g;int m=g.length,n=g[0].length;Queue<int[]> q=new ArrayDeque<>();for(int i=0;i<m;i++)for(int j=0;j<n;j++)if(g[i][j]==0)q.add(new int[]{i,j});int[][] D={{-1,0},{1,0},{0,-1},{0,1}};while(!q.isEmpty()){int[] p=q.poll();for(int[] d:D){int ni=p[0]+d[0],nj=p[1]+d[1];if(ni>=0&&nj>=0&&ni<m&&nj<n&&g[ni][nj]==INF){g[ni][nj]=g[p[0]][p[1]]+1;q.add(new int[]{ni,nj});}}}return g;}
  public static void main(String[]x){int[][] g={{INF,-1,0,INF},{INF,INF,INF,-1},{INF,-1,INF,-1},{0,-1,INF,INF}};System.out.println(Arrays.deepToString(walls(g)));}
}
