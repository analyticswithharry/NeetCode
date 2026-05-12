// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 143 -- Palindromic Substrings
// Category   : 1-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 72
// =============================================================
//
// QUESTION:
//   Count number of palindromic substrings in s.
// =============================================================
public class Lesson143_PalindromicSubstrings{
  static int count(String s){int c=0;for(int i=0;i<s.length();i++){c+=ex(s,i,i)+ex(s,i,i+1);}return c;}
  static int ex(String s,int a,int b){int c=0;while(a>=0&&b<s.length()&&s.charAt(a)==s.charAt(b)){c++;a--;b++;}return c;}
  public static void main(String[]x){System.out.println(count("abc"));System.out.println(count("aaa"));}
}
