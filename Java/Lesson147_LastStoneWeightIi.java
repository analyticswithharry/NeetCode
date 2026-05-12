// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 147 -- Last Stone Weight II
// Category   : 2-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 74
// =============================================================
//
// QUESTION:
//   Given stones, smash to minimize remaining weight (subset partition).
// =============================================================
public class Lesson147_LastStoneWeightIi{
  static int lsw2(int[]s){int t=0;for(int x:s)t+=x;int cap=t/2;boolean[] dp=new boolean[cap+1];dp[0]=true;for(int x:s)for(int j=cap;j>=x;j--)dp[j]=dp[j]||dp[j-x];for(int j=cap;j>=0;j--)if(dp[j])return t-2*j;return 0;}
  public static void main(String[]x){System.out.println(lsw2(new int[]{2,7,4,1,8,1}));System.out.println(lsw2(new int[]{31,26,33,21,40}));}
}
