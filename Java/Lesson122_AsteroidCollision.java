// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 122 -- Asteroid Collision
// Category   : Stack
// Difficulty : Medium
// Study Plan : Day 61
// =============================================================
//
// QUESTION:
//   Given an array of asteroids (positive=right, negative=left), return state after all collisions.
// =============================================================
import java.util.*;
public class Lesson122_AsteroidCollision{
  static int[] collide(int[]a){Deque<Integer> st=new ArrayDeque<>();outer: for(int x:a){while(!st.isEmpty()&&x<0&&st.peek()>0){if(st.peek()<-x){st.pop();continue;}else if(st.peek()==-x){st.pop();}continue outer;}st.push(x);}int[] r=new int[st.size()];for(int i=r.length-1;i>=0;i--)r[i]=st.pop();return r;}
  public static void main(String[]x){System.out.println(Arrays.toString(collide(new int[]{5,10,-5})));System.out.println(Arrays.toString(collide(new int[]{8,-8})));System.out.println(Arrays.toString(collide(new int[]{10,2,-5})));}
}
