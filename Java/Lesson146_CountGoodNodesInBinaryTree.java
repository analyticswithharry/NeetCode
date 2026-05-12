// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 146 -- Count Good Nodes In Binary Tree
// Category   : Trees
// Difficulty : Medium
// Study Plan : Day 73
// =============================================================
//
// QUESTION:
//   A node is good if no node on the root-to-node path has a value greater. Count good nodes.
// =============================================================
public class Lesson146_CountGoodNodesInBinaryTree{
  static class TN{int val;TN left,right;TN(int v){val=v;}TN(int v,TN l,TN r){val=v;left=l;right=r;}}
  static int rec(TN n,int m){if(n==null)return 0;int c=n.val>=m?1:0;int nm=Math.max(m,n.val);return c+rec(n.left,nm)+rec(n.right,nm);}
  static int good(TN r){return rec(r,Integer.MIN_VALUE);}
  public static void main(String[]x){TN r=new TN(3,new TN(1,new TN(3,null,null),null),new TN(4,new TN(1,null,null),new TN(5,null,null)));System.out.println(good(r));}
}
