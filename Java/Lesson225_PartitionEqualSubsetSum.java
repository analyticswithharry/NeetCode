// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 225 -- Partition Equal Subset Sum
// Category   : 1-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 113
// =============================================================
//
// QUESTION:
//   Can the array be split into two equal-sum subsets? Subset-sum DP.
// =============================================================
public class Lesson225_PartitionEqualSubsetSum{
  static boolean canPartition(int[] nums){int s=0;for(int x:nums)s+=x;if((s&1)==1)return false;int t=s/2;boolean[] dp=new boolean[t+1];dp[0]=true;for(int x:nums)for(int v=t;v>=x;v--)dp[v]=dp[v]||dp[v-x];return dp[t];}
  public static void main(String[]a){System.out.println(canPartition(new int[]{1,5,11,5}));}
}
