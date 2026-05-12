// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 213 -- Permutation in String
// Category   : Sliding Window
// Difficulty : Medium
// Study Plan : Day 107
// =============================================================
//
// QUESTION:
//   Return true if s2 contains a permutation of s1.
// =============================================================
public class Lesson213_PermutationInString{
  static boolean checkInclusion(String s1,String s2){if(s1.length()>s2.length())return false;int[] a=new int[26],b=new int[26];for(char c:s1.toCharArray())a[c-'a']++;for(int i=0;i<s2.length();i++){b[s2.charAt(i)-'a']++;if(i>=s1.length())b[s2.charAt(i-s1.length())-'a']--;if(java.util.Arrays.equals(a,b))return true;}return false;}
  public static void main(String[]a){System.out.println(checkInclusion("ab","eidbaooo"));System.out.println(checkInclusion("ab","eidboaoo"));}
}
