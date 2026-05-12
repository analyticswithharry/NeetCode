// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 128 -- Reverse Integer
// Category   : Bit Manipulation
// Difficulty : Medium
// Study Plan : Day 64
// =============================================================
//
// QUESTION:
//   Reverse digits of a signed 32-bit integer; return 0 on overflow.
// =============================================================
public class Lesson128_ReverseInteger{
  static int rev(int x){long r=0;while(x!=0){r=r*10+x%10;x/=10;}if(r<Integer.MIN_VALUE||r>Integer.MAX_VALUE)return 0;return (int)r;}
  public static void main(String[]a){System.out.println(rev(123));System.out.println(rev(-456));System.out.println(rev(1534236469));}
}
