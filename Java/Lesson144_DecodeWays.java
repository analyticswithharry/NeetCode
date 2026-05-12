// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 144 -- Decode Ways
// Category   : 1-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 72
// =============================================================
//
// QUESTION:
//   Number of ways to decode digit string s where '1'->A, ..., '26'->Z.
// =============================================================
public class Lesson144_DecodeWays{
  static int ways(String s){if(s==null||s.charAt(0)=='0')return 0;int n=s.length();int[] dp=new int[n+1];dp[0]=1;dp[1]=1;for(int i=2;i<=n;i++){if(s.charAt(i-1)!='0')dp[i]+=dp[i-1];int x=Integer.parseInt(s.substring(i-2,i));if(x>=10&&x<=26)dp[i]+=dp[i-2];}return dp[n];}
  public static void main(String[]x){System.out.println(ways("12"));System.out.println(ways("226"));System.out.println(ways("06"));}
}
