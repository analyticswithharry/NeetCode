// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 230 -- Integer Break
// Category   : 1-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 115
// =============================================================
//
// QUESTION:
//   Break n into >=2 positive ints; maximize product.
// =============================================================
public class Lesson230_IntegerBreak{
  static int integerBreak(int n){int[] dp=new int[n+1];dp[1]=1;for(int i=2;i<=n;i++)for(int j=1;j<i;j++)dp[i]=Math.max(dp[i],j*Math.max(i-j,dp[i-j]));return dp[n];}
  public static void main(String[]a){System.out.println(integerBreak(10));}
}
