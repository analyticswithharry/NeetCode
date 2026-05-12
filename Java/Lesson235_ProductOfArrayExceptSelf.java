// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 235 -- Product of Array Except Self
// Category   : Arrays and Hashing
// Difficulty : Medium
// Study Plan : Day 118
// =============================================================
//
// QUESTION:
//   Return array where output[i] = product of all nums except nums[i]. O(n) no division.
// =============================================================
public class Lesson235_ProductOfArrayExceptSelf{
  static int[] productExceptSelf(int[] n){int[] o=new int[n.length];int p=1;for(int i=0;i<n.length;i++){o[i]=p;p*=n[i];}p=1;for(int i=n.length-1;i>=0;i--){o[i]*=p;p*=n[i];}return o;}
  public static void main(String[]a){System.out.println(java.util.Arrays.toString(productExceptSelf(new int[]{1,2,3,4})));}
}
