// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 115 -- Plus One
// Category   : Math and Geometry
// Difficulty : Easy
// Study Plan : Day 58
// =============================================================
//
// QUESTION:
//   Given a non-empty array of decimal digits representing a non-negative integer, add one and return the resulting array.
// =============================================================
import java.util.*;
public class Lesson115_PlusOne{
  static int[] plusOne(int[]d){d=d.clone();for(int i=d.length-1;i>=0;i--){if(d[i]<9){d[i]++;return d;}d[i]=0;}int[] r=new int[d.length+1];r[0]=1;return r;}
  public static void main(String[]x){System.out.println(Arrays.toString(plusOne(new int[]{1,2,3})));System.out.println(Arrays.toString(plusOne(new int[]{9,9})));}
}
