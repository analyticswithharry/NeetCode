// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 119 -- Max Area of Island
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 60
// =============================================================
//
// QUESTION:
//   Given m x n binary grid, return max area of an island (4-directionally connected 1s).
// =============================================================
public class Lesson119_MaxAreaOfIsland{
  static int M,N; static int[][] G;
  static int dfs(int i,int j){if(i<0||j<0||i>=M||j>=N||G[i][j]!=1)return 0;G[i][j]=0;return 1+dfs(i+1,j)+dfs(i-1,j)+dfs(i,j+1)+dfs(i,j-1);}
  static int maxArea(int[][]g){G=g;M=g.length;N=g[0].length;int b=0;for(int i=0;i<M;i++)for(int j=0;j<N;j++)if(g[i][j]==1)b=Math.max(b,dfs(i,j));return b;}
  public static void main(String[]x){System.out.println(maxArea(new int[][]{{1,1,0},{1,0,0},{0,0,1}}));}
}
