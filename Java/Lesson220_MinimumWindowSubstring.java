// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 220 -- Minimum Window Substring
// Category   : Sliding Window
// Difficulty : Hard
// Study Plan : Day 110
// =============================================================
//
// QUESTION:
//   Smallest substring of s containing all chars of t.
// =============================================================
import java.util.*;
public class Lesson220_MinimumWindowSubstring{
  static String minWindow(String s,String t){if(t.isEmpty())return"";Map<Character,Integer> need=new HashMap<>();for(char c:t.toCharArray())need.merge(c,1,Integer::sum);Map<Character,Integer> have=new HashMap<>();int nn=need.size(),hn=0,l=0,rl=Integer.MAX_VALUE,rs=0,re=0;for(int r=0;r<s.length();r++){char c=s.charAt(r);have.merge(c,1,Integer::sum);if(need.containsKey(c)&&have.get(c).equals(need.get(c)))hn++;while(hn==nn){if(r-l+1<rl){rl=r-l+1;rs=l;re=r;}char d=s.charAt(l);have.put(d,have.get(d)-1);if(need.containsKey(d)&&have.get(d)<need.get(d))hn--;l++;}}return rl==Integer.MAX_VALUE?"":s.substring(rs,re+1);}
  public static void main(String[]a){System.out.println(minWindow("ADOBECODEBANC","ABC"));}
}
