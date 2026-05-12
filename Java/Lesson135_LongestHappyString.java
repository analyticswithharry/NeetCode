// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 135 -- Longest Happy String
// Category   : Heap Priority Queue
// Difficulty : Medium
// Study Plan : Day 68
// =============================================================
//
// QUESTION:
//   Given a,b,c counts of letters, build the longest string with at most a 'a', b 'b', c 'c' such that no three consecutive letters are equal.
// =============================================================
import java.util.*;
public class Lesson135_LongestHappyString{
  static String longest(int a,int b,int c){PriorityQueue<int[]> h=new PriorityQueue<>((p,q)->q[0]-p[0]);if(a>0)h.add(new int[]{a,'a'});if(b>0)h.add(new int[]{b,'b'});if(c>0)h.add(new int[]{c,'c'});StringBuilder sb=new StringBuilder();while(!h.isEmpty()){int[] x=h.poll();int n=sb.length();if(n>=2&&sb.charAt(n-1)==(char)x[1]&&sb.charAt(n-2)==(char)x[1]){if(h.isEmpty())break;int[] y=h.poll();sb.append((char)y[1]);if(y[0]-1>0)h.add(new int[]{y[0]-1,y[1]});h.add(x);}else{sb.append((char)x[1]);if(x[0]-1>0)h.add(new int[]{x[0]-1,x[1]});}}return sb.toString();}
  public static void main(String[]x){System.out.println(longest(1,1,7));System.out.println(longest(7,1,0));}
}
