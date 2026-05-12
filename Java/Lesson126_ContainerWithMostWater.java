// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 126 -- Container With Most Water
// Category   : Two Pointers
// Difficulty : Medium
// Study Plan : Day 63
// =============================================================
//
// QUESTION:
//   Given heights, find two lines that form the container holding most water.
// =============================================================
public class Lesson126_ContainerWithMostWater{
  static int maxArea(int[]h){int l=0,r=h.length-1,b=0;while(l<r){b=Math.max(b,(r-l)*Math.min(h[l],h[r]));if(h[l]<h[r])l++;else r--;}return b;}
  public static void main(String[]x){System.out.println(maxArea(new int[]{1,8,6,2,5,4,8,3,7}));}
}
