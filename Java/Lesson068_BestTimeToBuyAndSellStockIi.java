// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 068 -- Best Time to Buy and Sell Stock II
// Category   : Greedy
// Difficulty : Medium
// Study Plan : Day 34
// =============================================================
//
// QUESTION:
//   You may complete as many transactions as you like (buy then sell). Return max profit.
//
//   Example: [7,1,5,3,6,4] -> 7  (buy 1 sell 5, buy 3 sell 6)
// =============================================================

public class Lesson068_BestTimeToBuyAndSellStockIi {
    public int maxProfit(int[] prices){
        int p=0; for (int i=1;i<prices.length;i++) p += Math.max(0, prices[i]-prices[i-1]); return p;
    }
    public static void main(String[] a){ System.out.println(new Lesson068_BestTimeToBuyAndSellStockIi().maxProfit(new int[]{7,1,5,3,6,4})); }
}
