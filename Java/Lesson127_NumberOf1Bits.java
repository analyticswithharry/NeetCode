// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 127 -- Number of 1 Bits
// Category   : Bit Manipulation
// Difficulty : Easy
// Study Plan : Day 64
// =============================================================
//
// QUESTION:
//   Return the number of 1 bits in unsigned int.
// =============================================================
public class Lesson127_NumberOf1Bits{
  static int hw(int n){int c=0;while(n!=0){n&=n-1;c++;}return c;}
  public static void main(String[]x){System.out.println(hw(11));System.out.println(hw(128));}
}
