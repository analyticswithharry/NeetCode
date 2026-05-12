// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 226 -- Combination Sum IV
// Category   : 1-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 113
// =============================================================
//
// QUESTION:
//   Count ordered combinations of nums summing to target.
// =============================================================
public class Lesson226_CombinationSumIv{
  static int combSum4(int[] nums,int t){int[] dp=new int[t+1];dp[0]=1;for(int v=1;v<=t;v++)for(int x:nums)if(v>=x)dp[v]+=dp[v-x];return dp[t];}
  public static void main(String[]a){System.out.println(combSum4(new int[]{1,2,3},4));}
}
