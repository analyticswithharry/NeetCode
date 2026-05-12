// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 111 -- Single Number
// Category   : Bit Manipulation
// Difficulty : Easy
// Study Plan : Day 56
// =============================================================
//
// QUESTION:
//   Given a non-empty array of integers, every element appears twice except for one. Find that single one. O(1) extra space.
// =============================================================
public class Lesson111_SingleNumber{
  static int single(int[] a){int r=0;for(int x:a)r^=x;return r;}
  public static void main(String[] a){System.out.println(single(new int[]{2,2,1}));System.out.println(single(new int[]{4,1,2,1,2}));}
}
