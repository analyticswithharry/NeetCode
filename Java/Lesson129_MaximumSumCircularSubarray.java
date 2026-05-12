// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 129 -- Maximum Sum Circular Subarray
// Category   : Greedy
// Difficulty : Medium
// Study Plan : Day 65
// =============================================================
//
// QUESTION:
//   Given a circular integer array, find the maximum subarray sum (subarray may wrap).
// =============================================================
public class Lesson129_MaximumSumCircularSubarray{
  static int maxCirc(int[]a){int tot=0,mxc=a[0],cur=a[0],mnc=a[0],c2=a[0];for(int i=0;i<a.length;i++){if(i>0){cur=Math.max(a[i],cur+a[i]);mxc=Math.max(mxc,cur);c2=Math.min(a[i],c2+a[i]);mnc=Math.min(mnc,c2);}tot+=a[i];}return mxc<0?mxc:Math.max(mxc,tot-mnc);}
  public static void main(String[]x){System.out.println(maxCirc(new int[]{1,-2,3,-2}));System.out.println(maxCirc(new int[]{5,-3,5}));System.out.println(maxCirc(new int[]{-3,-2,-3}));}
}
