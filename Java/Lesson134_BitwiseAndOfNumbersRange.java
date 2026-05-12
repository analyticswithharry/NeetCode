// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 134 -- Bitwise AND of Numbers Range
// Category   : Bit Manipulation
// Difficulty : Medium
// Study Plan : Day 67
// =============================================================
//
// QUESTION:
//   Given range [m,n], return the bitwise AND of all numbers in this range, inclusive.
// =============================================================
public class Lesson134_BitwiseAndOfNumbersRange{
  static int rangeAnd(int m,int n){int s=0;while(m!=n){m>>=1;n>>=1;s++;}return m<<s;}
  public static void main(String[]x){System.out.println(rangeAnd(5,7));System.out.println(rangeAnd(0,0));}
}
