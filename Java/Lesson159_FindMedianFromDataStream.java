// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 159 -- Find Median From Data Stream
// Category   : Heap Priority Queue
// Difficulty : Hard
// Study Plan : Day 80
// =============================================================
//
// QUESTION:
//   Design MedianFinder: addNum, findMedian.
// =============================================================
import java.util.*;
public class Lesson159_FindMedianFromDataStream{
  static class MedianFinder{PriorityQueue<Integer> lo=new PriorityQueue<>(Comparator.reverseOrder());PriorityQueue<Integer> hi=new PriorityQueue<>();void addNum(int x){lo.add(x);hi.add(lo.poll());if(hi.size()>lo.size())lo.add(hi.poll());}double findMedian(){if(lo.size()>hi.size())return lo.peek();return (lo.peek()+hi.peek())/2.0;}}
  public static void main(String[]x){MedianFinder m=new MedianFinder();for(int v:new int[]{1,2,3}){m.addNum(v);System.out.println(m.findMedian());}}
}
