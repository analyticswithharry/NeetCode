// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 133 -- Counting Bits
// Category   : Bit Manipulation
// Difficulty : Easy
// Study Plan : Day 67
// =============================================================
//
// QUESTION:
//   For 0..n return array where ans[i] = number of 1-bits in i.
// =============================================================
import java.util.*;
public class Lesson133_CountingBits{
  static int[] cb(int n){int[] a=new int[n+1];for(int i=1;i<=n;i++)a[i]=a[i>>1]+(i&1);return a;}
  public static void main(String[]x){System.out.println(Arrays.toString(cb(5)));}
}
