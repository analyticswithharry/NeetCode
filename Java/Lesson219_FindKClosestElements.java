// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 219 -- Find K Closest Elements
// Category   : Sliding Window
// Difficulty : Medium
// Study Plan : Day 110
// =============================================================
//
// QUESTION:
//   Return k closest sorted ints to x (binary search the window).
// =============================================================
import java.util.*;
public class Lesson219_FindKClosestElements{
  static List<Integer> findClosest(int[] a,int k,int x){int l=0,r=a.length-k;while(l<r){int m=(l+r)>>1;if(x-a[m]>a[m+k]-x)l=m+1;else r=m;}List<Integer> res=new ArrayList<>();for(int i=l;i<l+k;i++)res.add(a[i]);return res;}
  public static void main(String[]a){System.out.println(findClosest(new int[]{1,2,3,4,5},4,3));}
}
