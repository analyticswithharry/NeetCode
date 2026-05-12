// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 114 -- Search In Rotated Sorted Array II
// Category   : Binary Search
// Difficulty : Medium
// Study Plan : Day 57
// =============================================================
//
// QUESTION:
//   Rotated sorted array may contain duplicates. Return true if target exists.
// =============================================================
public class Lesson114_SearchInRotatedSortedArrayIi{
  static boolean search(int[]a,int t){int lo=0,hi=a.length-1;while(lo<=hi){int m=(lo+hi)>>>1;if(a[m]==t)return true;if(a[lo]==a[m]&&a[m]==a[hi]){lo++;hi--;}else if(a[lo]<=a[m]){if(a[lo]<=t&&t<a[m])hi=m-1;else lo=m+1;}else{if(a[m]<t&&t<=a[hi])lo=m+1;else hi=m-1;}}return false;}
  public static void main(String[]x){System.out.println(search(new int[]{2,5,6,0,0,1,2},0));System.out.println(search(new int[]{2,5,6,0,0,1,2},3));}
}
