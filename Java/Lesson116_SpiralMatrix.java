// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 116 -- Spiral Matrix
// Category   : Math and Geometry
// Difficulty : Medium
// Study Plan : Day 58
// =============================================================
//
// QUESTION:
//   Given m x n matrix, return all elements in spiral order.
// =============================================================
import java.util.*;
public class Lesson116_SpiralMatrix{
  static List<Integer> spiral(int[][]m){List<Integer> r=new ArrayList<>();if(m.length==0)return r;int t=0,b=m.length-1,l=0,rg=m[0].length-1;while(t<=b&&l<=rg){for(int j=l;j<=rg;j++)r.add(m[t][j]);t++;for(int i=t;i<=b;i++)r.add(m[i][rg]);rg--;if(t<=b){for(int j=rg;j>=l;j--)r.add(m[b][j]);b--;}if(l<=rg){for(int i=b;i>=t;i--)r.add(m[i][l]);l++;}}return r;}
  public static void main(String[]x){System.out.println(spiral(new int[][]{{1,2,3},{4,5,6},{7,8,9}}));}
}
