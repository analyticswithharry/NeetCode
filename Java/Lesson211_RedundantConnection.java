// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 211 -- Redundant Connection
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 106
// =============================================================
//
// QUESTION:
//   Given an n-node tree with one extra edge (forming exactly one cycle), return the edge that can be removed.
// =============================================================
import java.util.*;
public class Lesson211_RedundantConnection{
  static int[] p;
  static int f(int x){while(p[x]!=x){p[x]=p[p[x]];x=p[x];}return x;}
  static int[] findRedundant(int[][] e){p=new int[e.length+1];for(int i=0;i<p.length;i++)p[i]=i;for(int[] x:e){int ra=f(x[0]),rb=f(x[1]);if(ra==rb)return x;p[ra]=rb;}return new int[0];}
  public static void main(String[]a){System.out.println(Arrays.toString(findRedundant(new int[][]{{1,2},{1,3},{2,3}})));}
}
