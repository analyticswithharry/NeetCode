// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 249 -- Serialize And Deserialize Binary Tree
// Category   : Trees
// Difficulty : Hard
// Study Plan : Day 125
// =============================================================
//
// QUESTION:
//   Pre-order serialize with null markers; queue-based deserialize.
// =============================================================
import java.util.*;
public class Lesson249_SerializeAndDeserializeBinaryTree{
  static class T{int v;T l,r;T(int v){this.v=v;}}
  static void dfs(T n,StringBuilder sb){if(n==null){sb.append("#,");return;}sb.append(n.v).append(',');dfs(n.l,sb);dfs(n.r,sb);}
  static String ser(T r){StringBuilder sb=new StringBuilder();dfs(r,sb);return sb.toString();}
  static int idx;static String[] arr;
  static T dfs2(){String x=arr[idx++];if(x.equals("#"))return null;T n=new T(Integer.parseInt(x));n.l=dfs2();n.r=dfs2();return n;}
  static T des(String s){arr=s.split(",");idx=0;return dfs2();}
  public static void main(String[]a){T r=new T(1);r.l=new T(2);r.r=new T(3);r.r.l=new T(4);r.r.r=new T(5);String s=ser(r);System.out.println(s);System.out.println(ser(des(s)));}
}
