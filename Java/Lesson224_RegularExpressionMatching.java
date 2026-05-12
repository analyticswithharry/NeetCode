// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 224 -- Regular Expression Matching
// Category   : 2-D Dynamic Programming
// Difficulty : Hard
// Study Plan : Day 112
// =============================================================
//
// QUESTION:
//   Implement regex with '.' and '*' (zero or more of preceding).
// =============================================================
public class Lesson224_RegularExpressionMatching{
  static boolean isMatch(String s,String p){int m=s.length(),n=p.length();boolean[][] dp=new boolean[m+1][n+1];dp[0][0]=true;for(int j=1;j<=n;j++)if(p.charAt(j-1)=='*')dp[0][j]=dp[0][j-2];for(int i=1;i<=m;i++)for(int j=1;j<=n;j++){if(p.charAt(j-1)=='.'||p.charAt(j-1)==s.charAt(i-1))dp[i][j]=dp[i-1][j-1];else if(p.charAt(j-1)=='*')dp[i][j]=dp[i][j-2]||((p.charAt(j-2)=='.'||p.charAt(j-2)==s.charAt(i-1))&&dp[i-1][j]);}return dp[m][n];}
  public static void main(String[]a){System.out.println(isMatch("aa","a*"));}
}
