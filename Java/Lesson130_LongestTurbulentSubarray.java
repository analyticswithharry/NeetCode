// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 130 -- Longest Turbulent Subarray
// Category   : Greedy
// Difficulty : Medium
// Study Plan : Day 65
// =============================================================
//
// QUESTION:
//   Given an array, return length of longest turbulent subarray (alternating > <).
// =============================================================
public class Lesson130_LongestTurbulentSubarray{
  static int turb(int[]a){int inc=1,dec=1,b=1;for(int i=1;i<a.length;i++){if(a[i]>a[i-1]){inc=dec+1;dec=1;}else if(a[i]<a[i-1]){dec=inc+1;inc=1;}else inc=dec=1;b=Math.max(b,Math.max(inc,dec));}return b;}
  public static void main(String[]x){System.out.println(turb(new int[]{9,4,2,10,7,8,8,1,9}));}
}
