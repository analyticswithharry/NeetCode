// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 132 -- Split Array Largest Sum
// Category   : Binary Search
// Difficulty : Hard
// Study Plan : Day 66
// =============================================================
//
// QUESTION:
//   Split nums into k non-empty contiguous parts to minimize the largest sum among parts.
// =============================================================
public class Lesson132_SplitArrayLargestSum{
  static boolean can(int[]a,int k,int mx){int c=1,s=0;for(int x:a){if(s+x>mx){c++;s=x;}else s+=x;}return c<=k;}
  static int split(int[]a,int k){int lo=0,hi=0;for(int x:a){lo=Math.max(lo,x);hi+=x;}while(lo<hi){int m=(lo+hi)>>>1;if(can(a,k,m))hi=m;else lo=m+1;}return lo;}
  public static void main(String[]x){System.out.println(split(new int[]{7,2,5,10,8},2));}
}
