// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 148 -- Best Time to Buy And Sell Stock With Cooldown
// Category   : 2-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 74
// =============================================================
//
// QUESTION:
//   Stock prices; can do unlimited transactions but after selling must cooldown 1 day. Max profit.
// =============================================================
public class Lesson148_BestTimeToBuyAndSellStockWithCooldown{
  static int maxP(int[]p){int hold=-p[0],sold=0,rest=0;for(int i=1;i<p.length;i++){int h=Math.max(hold,rest-p[i]);int s=hold+p[i];int r=Math.max(rest,sold);hold=h;sold=s;rest=r;}return Math.max(sold,rest);}
  public static void main(String[]x){System.out.println(maxP(new int[]{1,2,3,0,2}));}
}
