// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 149 -- Daily Temperatures
// Category   : Stack
// Difficulty : Medium
// Study Plan : Day 75
// =============================================================
//
// QUESTION:
//   For each day, return number of days until a warmer temperature, or 0.
// =============================================================
import java.util.*;
public class Lesson149_DailyTemperatures{
  static int[] dailyT(int[]t){int[] r=new int[t.length];Deque<Integer> st=new ArrayDeque<>();for(int i=0;i<t.length;i++){while(!st.isEmpty()&&t[st.peek()]<t[i]){int j=st.pop();r[j]=i-j;}st.push(i);}return r;}
  public static void main(String[]x){System.out.println(Arrays.toString(dailyT(new int[]{73,74,75,71,69,72,76,73})));}
}
