// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 136 -- Car Pooling
// Category   : Heap Priority Queue
// Difficulty : Medium
// Study Plan : Day 68
// =============================================================
//
// QUESTION:
//   Trips [numPassengers,from,to]; capacity. Return true iff possible to pick up & drop off all passengers without exceeding capacity.
// =============================================================
public class Lesson136_CarPooling{
  static boolean carPool(int[][]t,int cap){int[] e=new int[1001];for(int[] x:t){e[x[1]]+=x[0];e[x[2]]-=x[0];}int s=0;for(int v:e){s+=v;if(s>cap)return false;}return true;}
  public static void main(String[]x){System.out.println(carPool(new int[][]{{2,1,5},{3,3,7}},4));System.out.println(carPool(new int[][]{{2,1,5},{3,3,7}},5));}
}
