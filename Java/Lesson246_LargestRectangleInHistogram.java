// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 246 -- Largest Rectangle In Histogram
// Category   : Stack
// Difficulty : Hard
// Study Plan : Day 123
// =============================================================
//
// QUESTION:
//   Max rectangular area in histogram. Monotonic stack.
// =============================================================
import java.util.*;
public class Lesson246_LargestRectangleInHistogram{
  static int largestRect(int[] h){Deque<Integer> st=new ArrayDeque<>();int best=0;int[] h2=new int[h.length+1];System.arraycopy(h,0,h2,0,h.length);for(int i=0;i<h2.length;i++){while(!st.isEmpty()&&h2[st.peek()]>h2[i]){int top=st.pop();int w=st.isEmpty()?i:i-st.peek()-1;best=Math.max(best,h2[top]*w);}st.push(i);}return best;}
  public static void main(String[]a){System.out.println(largestRect(new int[]{2,1,5,6,2,3}));}
}
