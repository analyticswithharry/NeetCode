// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 152 -- Find The Duplicate Number
// Category   : Linked List
// Difficulty : Medium
// Study Plan : Day 76
// =============================================================
//
// QUESTION:
//   Array length n+1 with values in [1,n] containing one duplicate. Find it. O(1) extra space.
// =============================================================
public class Lesson152_FindTheDuplicateNumber{
  static int dup(int[]a){int s=a[0],f=a[0];do{s=a[s];f=a[a[f]];}while(s!=f);s=a[0];while(s!=f){s=a[s];f=a[f];}return s;}
  public static void main(String[]x){System.out.println(dup(new int[]{1,3,4,2,2}));System.out.println(dup(new int[]{3,1,3,4,2}));}
}
