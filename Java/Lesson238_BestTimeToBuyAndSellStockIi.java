// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 238 -- Best Time to Buy And Sell Stock II
// Category   : Arrays and Hashing
// Difficulty : Medium
// Study Plan : Day 119
// =============================================================
//
// QUESTION:
//   Multiple transactions allowed. Sum positive deltas.
// =============================================================
public class Lesson238_BestTimeToBuyAndSellStockIi{
  static int maxProfit(int[] p){int s=0;for(int i=1;i<p.length;i++)s+=Math.max(0,p[i]-p[i-1]);return s;}
  public static void main(String[]a){System.out.println(maxProfit(new int[]{7,1,5,3,6,4}));}
}
