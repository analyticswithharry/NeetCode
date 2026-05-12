// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 145 -- Construct Quad Tree
// Category   : Trees
// Difficulty : Medium
// Study Plan : Day 73
// =============================================================
//
// QUESTION:
//   Given an n x n grid of 0/1, build a quad tree representation. Return root.
// =============================================================
import java.util.*;
public class Lesson145_ConstructQuadTree{
  static class QN{boolean val,isLeaf;QN tl,tr,bl,br;QN(boolean v,boolean l){val=v;isLeaf=l;}}
  static int[][] G;
  static QN rec(int r,int c,int n){boolean same=true;for(int i=r;i<r+n;i++)for(int j=c;j<c+n;j++)if(G[i][j]!=G[r][c])same=false;if(same)return new QN(G[r][c]==1,true);int h=n/2;QN q=new QN(true,false);q.tl=rec(r,c,h);q.tr=rec(r,c+h,h);q.bl=rec(r+h,c,h);q.br=rec(r+h,c+h,h);return q;}
  static List<String> ser(QN n){List<String> r=new ArrayList<>();if(n.isLeaf){r.add(n.val?"1":"0");return r;}r.add("#");r.addAll(ser(n.tl));r.addAll(ser(n.tr));r.addAll(ser(n.bl));r.addAll(ser(n.br));return r;}
  public static void main(String[]x){G=new int[][]{{0,1},{1,0}};QN root=rec(0,0,2);System.out.println(ser(root));}
}
