// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 248 -- Detect Squares
// Category   : Math and Geometry
// Difficulty : Medium
// Study Plan : Day 124
// =============================================================
//
// QUESTION:
//   Add point or count axis-aligned squares with given query point.
// =============================================================
import java.util.*;
public class Lesson248_DetectSquares{
  static class DS{Map<Long,Integer> c=new HashMap<>();long k(int x,int y){return ((long)x<<32)|(y&0xFFFFFFFFL);}void add(int[] p){c.merge(k(p[0],p[1]),1,Integer::sum);}int count(int[] p){int x=p[0],y=p[1],tot=0;for(var e:new ArrayList<>(c.entrySet())){long key=e.getKey();int a=(int)(key>>32),b=(int)key;if(a==x||Math.abs(a-x)!=Math.abs(b-y))continue;tot+=e.getValue()*c.getOrDefault(k(a,y),0)*c.getOrDefault(k(x,b),0);}return tot;}}
  public static void main(String[]a){DS d=new DS();for(int[] p:new int[][]{{3,10},{11,2},{3,2}})d.add(p);System.out.println(d.count(new int[]{11,10}));}
}
