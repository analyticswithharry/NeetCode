// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 250 -- Stone Game III
// Category   : 1-D Dynamic Programming
// Difficulty : Hard
// Study Plan : Day 125
// =============================================================
//
// QUESTION:
//   Players take 1-3 stones from front; maximize own score. Return Alice/Bob/Tie.
// =============================================================
public class Lesson250_StoneGameIii{
  static String stoneGameIII(int[] s){int n=s.length;int[] dp=new int[n+1];for(int i=n-1;i>=0;i--){int best=Integer.MIN_VALUE,take=0;for(int k=0;k<3&&i+k<n;k++){take+=s[i+k];best=Math.max(best,take-dp[i+k+1]);}dp[i]=best;}return dp[0]>0?"Alice":dp[0]<0?"Bob":"Tie";}
  public static void main(String[]a){System.out.println(stoneGameIII(new int[]{1,2,3,7}));}
}
