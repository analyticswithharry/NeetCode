// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 214 -- Minimum Size Subarray Sum
// Category   : Sliding Window
// Difficulty : Medium
// Study Plan : Day 107
// =============================================================
//
// QUESTION:
//   Return the minimum length of a contiguous subarray whose sum is >= target. 0 if none.
// =============================================================
public class Lesson214_MinimumSizeSubarraySum{
  static int minSubArrayLen(int t,int[] n){int l=0,s=0,ans=Integer.MAX_VALUE;for(int r=0;r<n.length;r++){s+=n[r];while(s>=t){ans=Math.min(ans,r-l+1);s-=n[l++];}}return ans==Integer.MAX_VALUE?0:ans;}
  public static void main(String[]a){System.out.println(minSubArrayLen(7,new int[]{2,3,1,2,4,3}));}
}
