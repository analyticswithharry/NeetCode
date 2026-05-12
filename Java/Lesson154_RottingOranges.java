// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 154 -- Rotting Oranges
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 77
// =============================================================
//
// QUESTION:
//   0 empty, 1 fresh, 2 rotten. Each minute rotten infects 4-neighbor fresh. Min minutes to rot all, or -1.
// =============================================================
import java.util.*;
public class Lesson154_RottingOranges{
  static int rot(int[][]g){int m=g.length,n=g[0].length;Queue<int[]> q=new ArrayDeque<>();int fresh=0;for(int i=0;i<m;i++)for(int j=0;j<n;j++){if(g[i][j]==2)q.add(new int[]{i,j,0});else if(g[i][j]==1)fresh++;}int t=0;int[][] D={{-1,0},{1,0},{0,-1},{0,1}};while(!q.isEmpty()){int[] p=q.poll();t=p[2];for(int[] d:D){int ni=p[0]+d[0],nj=p[1]+d[1];if(ni>=0&&nj>=0&&ni<m&&nj<n&&g[ni][nj]==1){g[ni][nj]=2;fresh--;q.add(new int[]{ni,nj,p[2]+1});}}}return fresh>0?-1:t;}
  public static void main(String[]x){System.out.println(rot(new int[][]{{2,1,1},{1,1,0},{0,1,1}}));System.out.println(rot(new int[][]{{2,1,1},{0,1,1},{1,0,1}}));}
}
