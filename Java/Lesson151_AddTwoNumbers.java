// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 151 -- Add Two Numbers
// Category   : Linked List
// Difficulty : Medium
// Study Plan : Day 76
// =============================================================
//
// QUESTION:
//   Two non-empty linked lists (least-significant-digit first). Add and return sum as linked list.
// =============================================================
import java.util.*;
public class Lesson151_AddTwoNumbers{
  static class LN{int val;LN next;LN(int v){val=v;}}
  static LN add(LN a,LN b){LN d=new LN(0);LN cur=d;int c=0;while(a!=null||b!=null||c!=0){int v=c+(a!=null?a.val:0)+(b!=null?b.val:0);c=v/10;cur.next=new LN(v%10);cur=cur.next;if(a!=null)a=a.next;if(b!=null)b=b.next;}return d.next;}
  static LN fromArr(int[]x){LN d=new LN(0);LN c=d;for(int v:x){c.next=new LN(v);c=c.next;}return d.next;}
  static List<Integer> toList(LN n){List<Integer> r=new ArrayList<>();while(n!=null){r.add(n.val);n=n.next;}return r;}
  public static void main(String[]x){System.out.println(toList(add(fromArr(new int[]{2,4,3}),fromArr(new int[]{5,6,4}))));}
}
