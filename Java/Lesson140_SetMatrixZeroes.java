// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 140 -- Set Matrix Zeroes
// Category   : Math and Geometry
// Difficulty : Medium
// Study Plan : Day 70
// =============================================================
//
// QUESTION:
//   Given m x n matrix, if an element is 0, set its entire row and column to 0. In place.
// =============================================================
import java.util.*;
public class Lesson140_SetMatrixZeroes{
  static int[][] setZero(int[][]g){int m=g.length,n=g[0].length;boolean r0=false,c0=false;for(int j=0;j<n;j++)if(g[0][j]==0)r0=true;for(int i=0;i<m;i++)if(g[i][0]==0)c0=true;for(int i=1;i<m;i++)for(int j=1;j<n;j++)if(g[i][j]==0){g[i][0]=0;g[0][j]=0;}for(int i=1;i<m;i++)for(int j=1;j<n;j++)if(g[i][0]==0||g[0][j]==0)g[i][j]=0;if(r0)for(int j=0;j<n;j++)g[0][j]=0;if(c0)for(int i=0;i<m;i++)g[i][0]=0;return g;}
  public static void main(String[]x){System.out.println(Arrays.deepToString(setZero(new int[][]{{1,1,1},{1,0,1},{1,1,1}})));}
}
