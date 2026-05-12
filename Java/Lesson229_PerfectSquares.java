// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 229 -- Perfect Squares
// Category   : 1-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 115
// =============================================================
//
// QUESTION:
//   Min number of perfect-square numbers summing to n.
// =============================================================
public class Lesson229_PerfectSquares{
  static int numSquares(int n){int[] dp=new int[n+1];java.util.Arrays.fill(dp,Integer.MAX_VALUE);dp[0]=0;for(int i=1;i<=n;i++)for(int j=1;j*j<=i;j++)dp[i]=Math.min(dp[i],dp[i-j*j]+1);return dp[n];}
  public static void main(String[]a){System.out.println(numSquares(12));}
}
