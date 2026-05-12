// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 222 -- Candy
// Category   : Greedy
// Difficulty : Hard
// Study Plan : Day 111
// =============================================================
//
// QUESTION:
//   Each child gets >=1 candy; higher rating gets more than neighbors. Return min candies.
// =============================================================
public class Lesson222_Candy{
  static int candy(int[] r){int n=r.length;int[] a=new int[n];java.util.Arrays.fill(a,1);for(int i=1;i<n;i++)if(r[i]>r[i-1])a[i]=a[i-1]+1;for(int i=n-2;i>=0;i--)if(r[i]>r[i+1])a[i]=Math.max(a[i],a[i+1]+1);int s=0;for(int x:a)s+=x;return s;}
  public static void main(String[]a){System.out.println(candy(new int[]{1,0,2}));}
}
