// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 117 -- Meeting Rooms II
// Category   : Intervals
// Difficulty : Medium
// Study Plan : Day 59
// =============================================================
//
// QUESTION:
//   Given an array of meeting time intervals, return the minimum number of conference rooms required.
// =============================================================
import java.util.*;
public class Lesson117_MeetingRoomsIi{
  static int minRooms(int[][]it){Arrays.sort(it,(a,b)->a[0]-b[0]);PriorityQueue<Integer> h=new PriorityQueue<>();for(int[] x:it){if(!h.isEmpty()&&h.peek()<=x[0])h.poll();h.add(x[1]);}return h.size();}
  public static void main(String[]x){System.out.println(minRooms(new int[][]{{0,30},{5,10},{15,20}}));System.out.println(minRooms(new int[][]{{7,10},{2,4}}));}
}
