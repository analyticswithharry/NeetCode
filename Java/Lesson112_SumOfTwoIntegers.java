// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 112 -- Sum of Two Integers
// Category   : Bit Manipulation
// Difficulty : Medium
// Study Plan : Day 56
// =============================================================
//
// QUESTION:
//   Given two integers a and b, return the sum without using + or -.
// =============================================================
public class Lesson112_SumOfTwoIntegers{
  static int add(int a,int b){while(b!=0){int c=(a&b)<<1;a=a^b;b=c;}return a;}
  public static void main(String[]x){System.out.println(add(1,2));System.out.println(add(-2,3));}
}
