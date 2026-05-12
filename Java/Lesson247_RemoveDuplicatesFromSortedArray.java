// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 247 -- Remove Duplicates From Sorted Array
// Category   : Two Pointers
// Difficulty : Easy
// Study Plan : Day 124
// =============================================================
//
// QUESTION:
//   In-place dedupe of sorted array. Return new length.
// =============================================================
public class Lesson247_RemoveDuplicatesFromSortedArray{
  static int dedupe(int[] a){if(a.length==0)return 0;int k=1;for(int i=1;i<a.length;i++)if(a[i]!=a[k-1])a[k++]=a[i];return k;}
  public static void main(String[]a){int[] x={1,1,2,2,3};int n=dedupe(x);System.out.println(n);}
}
