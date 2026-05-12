// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 223 -- Burst Balloons
// Category   : 2-D Dynamic Programming
// Difficulty : Hard
// Study Plan : Day 112
// =============================================================
//
// QUESTION:
//   Burst balloons; coins = nums[l]*nums[i]*nums[r]. Maximize total.
// =============================================================
public class Lesson223_BurstBalloons{
  static int maxCoins(int[] nums){int n=nums.length+2;int[] a=new int[n];a[0]=1;a[n-1]=1;for(int i=0;i<nums.length;i++)a[i+1]=nums[i];int[][] dp=new int[n][n];for(int L=2;L<n;L++)for(int l=0;l+L<n;l++){int r=l+L;for(int i=l+1;i<r;i++)dp[l][r]=Math.max(dp[l][r],dp[l][i]+dp[i][r]+a[l]*a[i]*a[r]);}return dp[0][n-1];}
  public static void main(String[]a){System.out.println(maxCoins(new int[]{3,1,5,8}));}
}
