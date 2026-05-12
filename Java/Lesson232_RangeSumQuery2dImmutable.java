// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 232 -- Range Sum Query 2D Immutable
// Category   : Arrays and Hashing
// Difficulty : Medium
// Study Plan : Day 116
// =============================================================
//
// QUESTION:
//   Build prefix sum 2D for O(1) region queries.
// =============================================================
public class Lesson232_RangeSumQuery2dImmutable{
  static class NM{int[][] p;NM(int[][] m){int R=m.length,C=m[0].length;p=new int[R+1][C+1];for(int i=0;i<R;i++)for(int j=0;j<C;j++)p[i+1][j+1]=m[i][j]+p[i][j+1]+p[i+1][j]-p[i][j];}int sumRegion(int r1,int c1,int r2,int c2){return p[r2+1][c2+1]-p[r1][c2+1]-p[r2+1][c1]+p[r1][c1];}}
  public static void main(String[]a){NM n=new NM(new int[][]{{3,0,1},{5,6,3},{1,2,0}});System.out.println(n.sumRegion(0,0,2,2));System.out.println(n.sumRegion(1,1,2,2));}
}
