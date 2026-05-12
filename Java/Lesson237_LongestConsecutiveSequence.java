// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 237 -- Longest Consecutive Sequence
// Category   : Arrays and Hashing
// Difficulty : Medium
// Study Plan : Day 119
// =============================================================
//
// QUESTION:
//   Length of longest run of consecutive integers in unsorted array. O(n) hashset.
// =============================================================
import java.util.*;
public class Lesson237_LongestConsecutiveSequence{
  static int longestConsec(int[] n){Set<Integer> s=new HashSet<>();for(int x:n)s.add(x);int best=0;for(int x:s)if(!s.contains(x-1)){int y=x;while(s.contains(y+1))y++;best=Math.max(best,y-x+1);}return best;}
  public static void main(String[]a){System.out.println(longestConsec(new int[]{100,4,200,1,3,2}));}
}
