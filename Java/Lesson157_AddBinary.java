// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 157 -- Add Binary
// Category   : Bit Manipulation
// Difficulty : Easy
// Study Plan : Day 79
// =============================================================
//
// QUESTION:
//   Given two binary strings, return their sum as a binary string.
// =============================================================
public class Lesson157_AddBinary{
  static String addBin(String a,String b){int i=a.length()-1,j=b.length()-1,c=0;StringBuilder sb=new StringBuilder();while(i>=0||j>=0||c>0){int s=c+(i>=0?a.charAt(i--)-'0':0)+(j>=0?b.charAt(j--)-'0':0);sb.append(s%2);c=s/2;}return sb.reverse().toString();}
  public static void main(String[]x){System.out.println(addBin("11","1"));System.out.println(addBin("1010","1011"));}
}
