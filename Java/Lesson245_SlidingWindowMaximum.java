// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 245 -- Sliding Window Maximum
// Category   : Sliding Window
// Difficulty : Hard
// Study Plan : Day 123
// =============================================================
//
// QUESTION:
//   Max in each window of size k. Monotonic deque.
// =============================================================
import java.util.*;
public class Lesson245_SlidingWindowMaximum{
  static int[] maxSliding(int[] n,int k){Deque<Integer> dq=new ArrayDeque<>();int[] out=new int[n.length-k+1];int idx=0;for(int i=0;i<n.length;i++){while(!dq.isEmpty()&&n[dq.peekLast()]<=n[i])dq.pollLast();dq.add(i);if(dq.peek()<=i-k)dq.poll();if(i>=k-1)out[idx++]=n[dq.peek()];}return out;}
  public static void main(String[]a){System.out.println(Arrays.toString(maxSliding(new int[]{1,3,-1,-3,5,3,6,7},3)));}
}
