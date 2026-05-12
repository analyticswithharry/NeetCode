// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 160 -- IPO
// Category   : Heap Priority Queue
// Difficulty : Hard
// Study Plan : Day 80
// =============================================================
//
// QUESTION:
//   Pick at most k projects with capital >= w each. Each project gives profit; w grows. Maximize final w.
// =============================================================
import java.util.*;
public class Lesson160_Ipo{
  static int ipo(int k,int w,int[]p,int[]c){int n=p.length;int[][] proj=new int[n][2];for(int i=0;i<n;i++){proj[i][0]=c[i];proj[i][1]=p[i];}Arrays.sort(proj,(a,b)->a[0]-b[0]);PriorityQueue<Integer> h=new PriorityQueue<>(Comparator.reverseOrder());int i=0;for(int s=0;s<k;s++){while(i<n&&proj[i][0]<=w)h.add(proj[i++][1]);if(h.isEmpty())break;w+=h.poll();}return w;}
  public static void main(String[]x){System.out.println(ipo(2,0,new int[]{1,2,3},new int[]{0,1,1}));System.out.println(ipo(3,0,new int[]{1,2,3},new int[]{0,1,2}));}
}
