// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 118 -- Meeting Rooms III
// Category   : Intervals
// Difficulty : Hard
// Study Plan : Day 59
// =============================================================
//
// QUESTION:
//   Given n rooms (0..n-1) and meetings [start,end], assign meetings to lowest-numbered available room, delaying if needed (preserving duration). Return room hosting most meetings.
// =============================================================
import java.util.*;
public class Lesson118_MeetingRoomsIii{
  static int mostBooked(int n,int[][]m){Arrays.sort(m,(a,b)->a[0]-b[0]);PriorityQueue<Integer> free=new PriorityQueue<>();for(int i=0;i<n;i++)free.add(i);PriorityQueue<long[]> busy=new PriorityQueue<>((a,b)->a[0]!=b[0]?Long.compare(a[0],b[0]):Long.compare(a[1],b[1]));long[] cnt=new long[n];for(int[] x:m){while(!busy.isEmpty()&&busy.peek()[0]<=x[0]){free.add((int)busy.poll()[1]);}int r;long e;if(!free.isEmpty()){r=free.poll();e=x[1];}else{long[] top=busy.poll();r=(int)top[1];e=top[0]+x[1]-x[0];}busy.add(new long[]{e,r});cnt[r]++;}int mi=0;for(int i=1;i<n;i++)if(cnt[i]>cnt[mi])mi=i;return mi;}
  public static void main(String[]x){System.out.println(mostBooked(2,new int[][]{{0,10},{1,5},{2,7},{3,4}}));}
}
