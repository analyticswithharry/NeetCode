// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 150 -- Online Stock Span
// Category   : Stack
// Difficulty : Medium
// Study Plan : Day 75
// =============================================================
//
// QUESTION:
//   Implement StockSpanner.next(price): consecutive days <= today's price (including today).
// =============================================================
import java.util.*;
public class Lesson150_OnlineStockSpan{
  static class StockSpanner{Deque<int[]> st=new ArrayDeque<>();int next(int p){int s=1;while(!st.isEmpty()&&st.peek()[0]<=p)s+=st.pop()[1];st.push(new int[]{p,s});return s;}}
  public static void main(String[]x){StockSpanner s=new StockSpanner();int[] arr={100,80,60,70,60,75,85};StringBuilder sb=new StringBuilder("[");for(int v:arr){sb.append(s.next(v)).append(" ");}sb.append("]");System.out.println(sb);}
}
